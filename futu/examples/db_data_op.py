# -*- coding: utf-8 -*-
"""
Examples for use the python functions: get data
"""
from operator import gt
import sqlite3
import platform
import time

class GetTickData():
    def __init__(self,stock_code):
        self.stock_code  = stock_code.split('.')[1]
        
        if platform.system() == "Windows":
            self.sqlitedb_order = sqlite3.connect(u"D:\\StockData\\stock_order.db")
            self.sqlitedb_tick  = sqlite3.connect(u"D:\\StockData\\stock_tick.db")
            self.sqlitedb_quote = sqlite3.connect(u"D:\\StockData\\stock_quote.db")
            self.sqlitedb_rt    = sqlite3.connect(u"D:\\StockData\\stock_rt.db")
            self.sqlitedb_war   = sqlite3.connect(u"D:\\StockData\\stock_warrant.db")
        else:
            self.sqlitedb_order = sqlite3.connect(u"/data/ft_hist_data/tick_data_20220420/stock_order.db")
            self.sqlitedb_tick  = sqlite3.connect(u"/data/ft_hist_data/tick_data_20220420/stock_tick.db")
            self.sqlitedb_quote = sqlite3.connect(u"/data/ft_hist_data/tick_data_20220420/stock_quote.db")
            self.sqlitedb_rt    = sqlite3.connect(u"/data/ft_hist_data/tick_data_20220420/stock_rt.db")
            self.sqlitedb_war   = sqlite3.connect(u"/data/ft_hist_data/tick_data_20220420/stock_warrant.db")

    def __del__(self):
        pass
        # self.sqlitedb_order.close()
        # self.sqlitedb_tick.close()
        # self.sqlitedb_quote.close()
        # self.sqlitedb_rt.close()

    def exe_sql(self,sql_cmd,db='tick'):
        if db == "tick":
            cu = self.sqlitedb_tick.cursor()
        elif db == "quote":
            cu = self.sqlitedb_quote.cursor()
        elif db == "rt":
            cu = self.sqlitedb_rt.cursor()
        elif db == "war":
            cu = self.sqlitedb_war.cursor()
        else:
            cu = self.sqlitedb_order.cursor()
        #print(sql_cmd)
        cu.execute(sql_cmd)
        if db == "tick":
            self.sqlitedb_tick.commit()
        elif db == "quote":
            self.sqlitedb_quote.commit()
        elif db == "rt":
            self.sqlitedb_rt.commit()
        elif db == "war":
            self.sqlitedb_war.commit()
        else:
            self.sqlitedb_order.commit()
        return cu.fetchall()

    def exe_sql_many(self,sql_cmd,insertDataList,db='tick'):
        if db == "tick":
            cu = self.sqlitedb_tick.cursor()
        elif db == "quote":
            cu = self.sqlitedb_quote.cursor()
        elif db == "rt":
            cu = self.sqlitedb_rt.cursor()
        elif db == "war":
            cu = self.sqlitedb_war.cursor()
        else:
            cu = self.sqlitedb_order.cursor()
        #print("begin to insert data length is [%s]" % len(insertDataList))
        #print(sql_cmd)
        #print(insertDataList)
        cu.executemany(sql_cmd,insertDataList)
        if db == "tick":
            self.sqlitedb_tick.commit()
        elif db == "quote":
            self.sqlitedb_quote.commit()
        elif db == "rt":
            self.sqlitedb_rt.commit()
        elif db == "war":
            self.sqlitedb_war.commit()
        else:
            self.sqlitedb_order.commit()
        return cu.fetchall()

if __name__ == "__main__":
    gtd_obj = GetTickData('HK.00700')
    dt = gtd_obj.exe_sql(sql_cmd="select * from tick_data_00700 limit 5", db='tick')
    print(type(dt[0][6]))