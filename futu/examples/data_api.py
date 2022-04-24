import logging
import random

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

def get_k_line(symbol, ):
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    ret, data, page_req_key = quote_ctx.request_history_kline('HK.00700', start='2019-09-11', end='2019-09-18', max_count=5)  # 每页5个，请求第一页
    if ret == RET_OK:
        print(data)
        print(data['code'][0])    # 取第一条的股票代码
        print(data['close'].values.tolist())   # 第一页收盘价转为 list
    else:
        print('error:', data)
    while page_req_key != None:  # 请求后面的所有结果
        print('*************************************')
        ret, data, page_req_key = quote_ctx.request_history_kline('HK.00700', start='2019-09-11', end='2019-09-18', max_count=5, page_req_key=page_req_key) # 请求翻页后的数据
        if ret == RET_OK:
            print(data)
        else:
            print('error:', data)
    print('All pages are finished!')
    quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽




@app.route('/')
def hello_world():
    return jsonify({"code": 404, "data": {}, "msg": "您访问的路径不存在哦！"})


@app.route('/get_data')
def get_data():
    """
    http://customserver:80/data?symbol=BTC_USD_OKCoin_EN&eid=OKCoin_EN&round=3&vround=3&period=900000&from=1564315200&to=1567267200
    """
    app.logger.info(request.args)

    symbol = request.args.get('symbol', None)
    eid = request.args.get('eid', None)
    price_round = int(request.args.get('round', 5))
    price_vround = int(request.args.get('vround', 0))
    vround = int(request.args.get('period', 0))
    depth = int(request.args.get('depth', 5))
    trades = request.args.get('trades', 0)
    ts_from = int(request.args.get('from', 0))
    ts_to = int(request.args.get('to', 0))

    app.logger.info(request.args)

    ts = ts_from + 60 * 60 * 5
    dt_list = []
    while ts < ts_to:
        sell_price = 90000+random.randint(0, 5000)
        dt_list.append(            
            [ts*1000, 100000+random.randint(0, 1000),80000+random.randint(0, 1000),sell_price, sell_price-1,787]
        )
        ts += 60

    ret_data = {
        "schema": ["time","open","high","low","close","vol"],
        "data": dt_list
    }
    app.logger.debug(ret_data)
    return jsonify(ret_data)


if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    # 设置日志记录最低级别为DEBUG，低于DEBUG级别的日志记录会被忽略，不设置setLevel()则默认为NOTSET级别。
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port='8080')
