import logging
import random
import sqlite3
import futu as ft
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/get_kline')
def get_k_line():
    symbol = request.args.get('symbol', None)
    ktype = request.args.get('ktype', None)
    start_date = request.args.get('start_date', None)
    end_date = request.args.get('end_date', None)
    quote_ctx = ft.OpenQuoteContext(host='127.0.0.1', port=11111)
    result_list = []

    ret, data, page_req_key = quote_ctx.request_history_kline(code=symbol,start=start_date, end=end_date, ktype=ktype, max_count=1000)  # 每页5个，请求第一页
    if ret == ft.RET_OK:
        for index, row in data.iterrows():          
            result_list.append([
                row['time_key'],
                row['open'],
                row['low'],
                row['high'],
                row['close'],
                row['volume']  
            ])       
    else:
        print('error:', data)
        return jsonify(result_list)

    while page_req_key != None:  # 请求后面的所有结果
        print('*************************************')
        ret, data, page_req_key = quote_ctx.request_history_kline(code=symbol,start=start_date,end=end_date,ktype=ktype, max_count=1000, page_req_key=page_req_key) # 请求翻页后的数据
        if ret == ft.RET_OK:
            for index, row in data.iterrows():
                result_list.append([
                    row['time'],
                    row['open'],
                    row['low'],
                    row['high'],
                    row['close'],
                    row['volume']  
                ])       
        else:
            print('error:', data)
            continue

    print('All pages are finished!')
    quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
    return jsonify(result_list)


@app.route('/get_seconds_kline')
def get_seconds_kline():
    app.logger.info(request.args)
    symbol = request.args.get('symbol', None)
    ktype = request.args.get('ktype', None)
    start_time = request.args.get('start_time', None)
    end_time = request.args.get('end_time', None)

    sqlitedb_kline = sqlite3.connect(f"/data/ft_hist_data/push_data/stock_kline_{symbol}.db")
    if not start_time:
        start_time = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    if not end_time:
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql_cmd = f" select * from stock_kline_{ktype}_{symbol} where time between '{start_time}' and '{end_time}'"
    app.logger.debug(sql_cmd)

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    sqlitedb_kline.row_factory = dict_factory
    cu = sqlitedb_kline.cursor()        
    cu.execute(sql_cmd)       
    result_list = []
    for line in cu.fetchall():
        result_list.append(line)
    
    return jsonify(result_list)


@app.route('/get_simple_kline')
def get_simple_kline():
    app.logger.info(request.args)
    symbol = request.args.get('symbol', None)
    ktype = request.args.get('ktype', None)
    start_time = request.args.get('start_time', None)
    end_time = request.args.get('end_time', None)

    sqlitedb_kline = sqlite3.connect(f"/data/ft_hist_data/push_data/stock_kline_{symbol}.db")
    if not start_time:
        start_time = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
    if not end_time:
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql_cmd = f" select * from stock_kline_{ktype}_{symbol} where time between '{start_time}' and '{end_time}'"
    app.logger.debug(sql_cmd)

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    sqlitedb_kline.row_factory = dict_factory
    cu = sqlitedb_kline.cursor()        
    cu.execute(sql_cmd)       
    result_list = []
    for line in cu.fetchall():       
        result_list.append([
            line['time'],
            line['open'],
            line['low'],
            line['high'],
            line['close'],
            line['volume']            
        ])
    
    return jsonify(result_list)


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
    app.run(host='0.0.0.0', port='8000')
