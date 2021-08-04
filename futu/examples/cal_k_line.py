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
import numpy as np

class CalKline(object):
    """
    k_type: ns|nm eg: 3s 5s  1m 5m 15m
    """
    def __init__(self, stock_code, cal_date=None, k_type='3s'):
        self.stock_code  = stock_code.split('.')[1]
        self.k_type = k_type       
        self.k_line_table_name = "stock_kline_%s_%s" % (k_type, self.stock_code)
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
        sql_cmd_create = """create TABLE IF NOT EXISTS  %s ( 
                            [time] TIME, 
                            [open] FLOAT, 
                            [close] FLOAT, 
                            [high] FLOAT, 
                            [low] FLOAT, 
                            [volume] INT, 
                            [turnover] FLOAT,
                            [buy_volume] INT,  
                            [sell_volume] INT, 
                            [neutral_volume] INT, 
                            PRIMARY KEY([time])) """ % self.k_line_table_name
        self.exe_sql(sql_cmd_create, db=self.sqlitedb_kline)

    def delete_kline_data(self):
        sql_cmd_delete = """ delete from stock_kline_%s where date(time)='%s' """ % (self.stock_code, self.cal_date)
        self.exe_sql(sql_cmd_delete, db=self.sqlitedb_kline)

    def get_timestamp(self, freq='3s'):
        morning_df = pd.date_range(start='%s 09:30:00' % self.cal_date, end='%s 12:00:00' % self.cal_date, freq=freq, normalize=False)
        afternoon_df = pd.date_range(start='%s 13:00:00' % self.cal_date, end='%s 16:00:00' % self.cal_date, freq=freq, normalize=False)
        time_list = []
        for line in morning_df.to_list() + afternoon_df.to_list():
            time_list.append(str(line))
        return time_list


    def calculate(self):
        query_sql =  """ select * from tick_data_%s 
                         where time>'%s 00:00:00' and time<'%s 23:59:59' 
                         order by time """ % (self.stock_code, self.cal_date, self.cal_date)

        df = pd.read_sql(query_sql, self.sqlitedb_tick)
        df = df.set_index(pd.DatetimeIndex(pd.to_datetime(df.time)))

        df_price_ohlc = df['price'].resample(self.k_type, label='right').ohlc()
        df_volume_df = df['volume'].resample(self.k_type, label='right').sum()
        df_turnover = df['turnover'].resample(self.k_type, label='right').sum()

        df_buy_volume = df[df['ticker_direction']=='BUY']['volume'].resample(self.k_type, label='right').sum()
        df_buy_volume.rename('buy_volume', inplace=True)
       
        df_sell_volume = df[df['ticker_direction']=='SELL']['volume'].resample(self.k_type, label='right').sum()
        df_sell_volume.rename('sell_volume', inplace=True)
        df_neutral_volume = df[df['ticker_direction']=='NEUTRAL']['volume'].resample(self.k_type, label='right').sum()
        df_neutral_volume.rename('neutral_volume', inplace=True)

        df_all = pd.merge(df_price_ohlc, df_volume_df, on=['time'])       
        df_all = pd.merge(df_all, df_turnover, on=['time'])
        df_all = pd.merge(df_all, df_buy_volume, on=['time'])
        df_all = pd.merge(df_all, df_sell_volume, on=['time'])
        df_all = pd.merge(df_all, df_neutral_volume, on=['time'])
        print("save stock[%s] ktype [%s] line num [%s] to table [%s]" % (self.stock_code, self.k_type, len(df_all), self.k_line_table_name))     
        df_all.to_sql(name=self.k_line_table_name, con=self.sqlitedb_kline, if_exists='append', index=True)

def cal_all_stock_kline()       

if __name__ == "__main__":
    cal_obj = CalKline('HK.00700', cal_date='2020-10-12', k_type='3s')
    cal_obj.delete_kline_data()
    cal_obj.calculate()
    