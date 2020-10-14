#!/usr/bin/env python
# encoding: utf-8
'''
@author: encorexiao@futunn.com
@file: cal_k_line.py
@time: 2020/10/13 20:46
@desc:
'''

import sqlite3
import platform
import time
from datetime import datetime
import pandas as pd

class CalKline(object):
    """
    k_type: ns|nm eg: 3s 5s  1m 5m 15m
    """
    def __init__(self, stock_code, cal_date=None, k_type='3s'):
        self.stock_code  = stock_code.split('.')[1]
        if cal_date:
            self.cal_date = cal_date
        else:
            self.cal_date = datetime.now().strftime('%Y%m%d')

        if platform.system() == "Windows":
            self.sqlitedb_tick  = sqlite3.connect(u"D:\\StockData\\stock_tick.db")
            self.sqlitedb_kline = sqlite3.connect(u"D:\\StockData\\stock_kline.db")
        else:
            self.sqlitedb_tick  = sqlite3.connect(u"/data/ft_hist_data/tick_data/stock_tick.db")
            self.sqlitedb_kline = sqlite3.connect(u"/data/ft_hist_data/tick_data/stock_kline.db")

    def __del__(self):
        self.sqlitedb_kline.close()
        self.sqlitedb_tick.close()

    def exe_sql(self, sql_cmd, db='tick'):
        if db == "tick":
            cu = self.sqlitedb_tick.cursor()
        else:
            cu = self.sqlitedb_kline.cursor()
        #print(sql_cmd)
        cu.execute(sql_cmd)
        if db == "tick":
            self.sqlitedb_tick.commit()
        else:
            self.sqlitedb_kline.commit()
        return cu.fetchall()

    def exe_sql_many(self,sql_cmd, insertDataList, db='tick'):
        if db == "tick":
            cu = self.sqlitedb_tick.cursor()
        else:
            cu = self.sqlitedb_kline.cursor()

        cu.executemany(sql_cmd, insertDataList)
        if db == "tick":
            self.sqlitedb_tick.commit()
        else:
            self.sqlitedb_kline.commit()
        return cu.fetchall()

    def create_kline_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  stock_kline_%s (                          
                            [f_date] DATE,
                            [f_time] TIME, 
                            [open_price] FLOAT, 
                            [close_price] FLOAT, 
                            [high_price] FLOAT, 
                            [low_price] FLOAT, 
                            [volume] INT, 
                            [turnover] FLOAT,
                            [direction] INT,  
                            PRIMARY KEY([f_date], [f_time])) """ % self.stock_code
        self.exe_sql(sql_cmd_create, db=self.sqlitedb_kline)

    def calculate(self):
        query_sql =  """ select * from tick_data_%s 
                         where time>'%s 00:00:00' and time<'%s 23:59:59' 
                         order by time """ % (self.stock_code, self.cal_date, self.cal_date)

        df = pd.read_sql(query_sql, self.sqlitedb_tick )

        # tick_data = self.exe_sql(query_sql, db='tick')
        #
        # last_datetime = None
        #
        # default_dict = {
        #     "open_price": 0,
        #     "close_price": 0,
        #     "high_price": 0,
        #     "low_price": 0,
        #     "volume": 0,
        #     "turnover": 0,
        #     "direction": 0,  # 0 sell 1 buy
        #     "buy_volume": 0,
        #     "sell_volume": 0,
        #     "buy_turnover": 0,
        #     "sell_turnover": 0
        # }

        #df = DataFrame(tick_data)
        #df.columns = resoverall.keys()


        # for tick in tick_data:
        #     f_date = tick.time.strftime('%Y-%m-d')
        #     if (tick_time - last_datetime)

if __name__ == "__main__":
    cal_obj = CalKline('00700', cal_date='2020-10-12')