import time
from futu import *
from sqlalchemy import create_engine
from filter_stock import FilterStock

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

engine = create_engine('sqlite:///save_pandas.db', echo=False)
sqlite_connection = engine.connect()
sqlite_table = "SnapshotData"

code_list = FilterStock(quote_ctx).get_hk_val_top()

while True:
    ret, data = quote_ctx.get_market_snapshot(code_list)
    if ret == RET_OK:        
        #print(data['code'][0])                # 取第一条的股票代码
        #print(data['code'].values.tolist())   # 转为 list
        #data.insert(data.shape[1], 'dt', time.time())
        data['save_datetime'] = time.time()
        data.to_sql(sqlite_table, sqlite_connection, if_exists='append', index=True)
    else:
        print('error:', data)
    print(f"time to save data {time.time()}")
    time.sleep(3)

quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
sqlite_connection.close()
