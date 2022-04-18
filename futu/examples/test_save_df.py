import time
from futu import *
from sqlalchemy import create_engine

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

engine = create_engine('sqlite:///save_pandas.db', echo=True)
sqlite_connection = engine.connect()
sqlite_table = "Covid19"

while True:
    ret, data = quote_ctx.get_market_snapshot(['SH.600000', 'HK.00700'])
    if ret == RET_OK:
        print(data)
        print(data['code'][0])                # 取第一条的股票代码
        print(data['code'].values.tolist())   # 转为 list
        data.to_sql(sqlite_table, sqlite_connection, if_exists='append', index=True)
    else:
        print('error:', data)
        
    time.sleep(1)

quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
sqlite_connection.close()