import logging
import random

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


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
