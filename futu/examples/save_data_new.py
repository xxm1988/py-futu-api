# -*- coding: utf-8 -*-
"""
Save Push Data
"""
from time import sleep
import futu as ft
import json
import talib
import sqlite3
import platform
import time
from datetime import datetime
import multiprocessing

class SaveDailyInfoData():
    def __init__(self, data_date=None):        
        if data_date:
            self.data_date = data_date
        else:
            self.data_date = datetime.now().strftime('%Y%m%d')

        if platform.system() == "Windows":     
            self.sqlitedb   = sqlite3.connect(u"D:\\StockData\\stock_daily_info.db")
        else:            
            self.sqlitedb   = sqlite3.connect(u"/data/ft_hist_data/push_data/stock_daily_info.db")

    def __del__(self):              
        self.sqlitedb.close()

    def exe_sql(self,sql_cmd):        
        cu = self.sqlitedb.cursor()       
        #print(sql_cmd)
        cu.execute(sql_cmd)
        self.sqlitedb.commit()        
        return cu.fetchall()
    
    def create_daily_info_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  stock_daily_info (                          
                            [date] DATE,
                            [top_val_list] TEXT, 
                            [top_turn_over_list] TEXT,                           
                            PRIMARY KEY([code], [date])) """
        self.exe_sql(sql_cmd_create)
  
    def save_data_daily_info(self, top_val_list, top_turn_over_list):
        sql_cmd = """ replace into stock_daily_info(date,top_val_list,top_turn_over_list) values('%s','%s','%s') 
        """ % (datetime.now().strftime('%Y-%m-%d'),json.dumps(top_val_list),json.dumps(top_turn_over_list))
        result = self.exe_sql(sql_cmd)
        return result


class SaveWarrantData():
    def __init__(self, data_date=None):        
        if data_date:
            self.data_date = data_date
        else:
            self.data_date = datetime.now().strftime('%Y%m%d')

        if platform.system() == "Windows":     
            self.sqlitedb_war   = sqlite3.connect(u"D:\\StockData\\stock_warrant.db")
        else:            
            self.sqlitedb_war   = sqlite3.connect(u"/data/ft_hist_data/push_data/stock_warrant.db")

    def __del__(self):              
        self.sqlitedb_war.close()

    def exe_sql(self,sql_cmd):        
        cu = self.sqlitedb_war.cursor()       
        #print(sql_cmd)
        cu.execute(sql_cmd)
        self.sqlitedb_war.commit()        
        return cu.fetchall()
    
    def create_warrant_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  stock_ref_warrant (
                            [code] TEXT,
                            [date] DATE,                           
                            [bull_list] TEXT,                          
                            [bear_list] TEXT,
                            PRIMARY KEY([code], [date])) """
        self.exe_sql(sql_cmd_create,db='war')
  
    def save_data_warrant(self, stock_code, bull_list, bear_list):
        sql_cmd = """ replace into stock_ref_warrant(code,date,bull_list,bear_list) values('%s','%s','%s','%s') 
        """ % (stock_code,datetime.now().strftime('%Y-%m-%d'),json.dumps(bull_list),json.dumps(bear_list))
        result = self.exe_sql(sql_cmd,db='war')
        return result


class SavePushData():
    def __init__(self,stock_code,data_date=None):
        self.stock_code  = stock_code.split('.')[1]
        if data_date:
            self.data_date = data_date
        else:
            self.data_date = datetime.now().strftime('%Y%m%d')

        if platform.system() == "Windows":           
            self.sqlitedb_tick  = sqlite3.connect(u"D:\\StockData\\stock_tick_%s.db" % self.stock_code)
            self.sqlitedb_quote = sqlite3.connect(u"D:\\StockData\\stock_quote_%s.db" % self.stock_code)
            self.sqlitedb_rt    = sqlite3.connect(u"D:\\StockData\\stock_rt_%s.db" % self.stock_code)           
        else:            
            self.sqlitedb_tick  = sqlite3.connect(u"/data/ft_hist_data/ls/stock_tick_%s.db" % self.stock_code)
            self.sqlitedb_quote = sqlite3.connect(u"/data/ft_hist_data/push_data/stock_quote_%s.db" % self.stock_code)
            self.sqlitedb_rt    = sqlite3.connect(u"/data/ft_hist_data/push_data/stock_rt_%s.db" % self.stock_code)
            
    def __del__(self):      
        self.sqlitedb_tick.close()
        self.sqlitedb_quote.close()
        self.sqlitedb_rt.close()

    def exe_sql(self,sql_cmd,db='tick'):
        if db == "tick":
            cu = self.sqlitedb_tick.cursor()
        elif db == "quote":
            cu = self.sqlitedb_quote.cursor()
        elif db == "rt":
            cu = self.sqlitedb_rt.cursor()      
        else:
            return None

        #print(sql_cmd)
        cu.execute(sql_cmd)
        if db == "tick":
            self.sqlitedb_tick.commit()
        elif db == "quote":
            self.sqlitedb_quote.commit()
        elif db == "rt":
            self.sqlitedb_rt.commit()      
        else:
            return None
            #self.sqlitedb_order.commit()
        return cu.fetchall()

    def exe_sql_many(self,sql_cmd,insertDataList,db='tick'):
        if db == "tick":
            cu = self.sqlitedb_tick.cursor()
        elif db == "quote":
            cu = self.sqlitedb_quote.cursor()
        elif db == "rt":
            cu = self.sqlitedb_rt.cursor()
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
        else:
            self.sqlitedb_order.commit()
        return cu.fetchall()

    def create_tick_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  tick_data_%s (
                            [code] TEXT,
                            [time] DATETIME,
                            [price] FLOAT,
                            [volume] INT,
                            [turnover] FLOAT,
                            [ticker_direction] TEXT,
                            [sequence] BIGINT,
                            [type] TEXT,
                            [push_data_type] TEXT) """  % self.stock_code
        self.exe_sql(sql_cmd_create,db='tick')

    def create_rt_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  rt_data_%s (                        
                            [code] TEXT,
                            [time] DATETIME,
                            [is_blank] INTERGET,
                            [opened_mins] INTERGET,
                            [cur_price] FLOAT,
                            [last_close] FLOAT,
                            [avg_price] FLOAT,
                            [turnover] FLOAT,
                            [volume] FLOAT,
                            [save_time] FLOAT) """  % self.stock_code
        self.exe_sql(sql_cmd_create,db='rt')

    def create_quote_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  quote_data_%s (
                            [code] CHAR NOT NULL, 
                            [data_date] DATE, 
                            [data_time] TIME, 
                            [last_price] FLOAT, 
                            [open_price] FLOAT, 
                            [high_price] FLOAT, 
                            [low_price] FLOAT, 
                            [prev_close_price] FLOAT, 
                            [volume] INT, 
                            [turnover] FLOAT, 
                            [turnover_rate] FLOAT, 
                            [amplitude] INT, 
                            [suspension] INT, 
                            [listing_date] DATE, 
                            [price_spread] FLOAT, 
                            [dark_status] CHAR, 
                            [sec_status] CHAR, 
                            [strike_price] FLOAT, 
                            [contract_size] INT, 
                            [open_interest] INT, 
                            [implied_volatility] FLOAT, 
                            [premium] FLOAT, 
                            [delta] FLOAT, 
                            [gamma] FLOAT, 
                            [vega] FLOAT, 
                            [theta] FLOAT, 
                            [rho] FLOAT, 
                            [net_open_interest] INT, 
                            [expiry_date_distance] INT, 
                            [contract_nominal_value] FLOAT, 
                            [owner_lot_multiplier] FLOAT, 
                            [option_area_type] CHAR, 
                            [contract_multiplier] FLOAT, 
                            [pre_price] FLOAT, 
                            [pre_high_price] FLOAT, 
                            [pre_low_price] FLOAT, 
                            [pre_volume] FLOAT, 
                            [pre_turnover] FLOAT, 
                            [pre_change_val] FLOAT, 
                            [pre_change_rate] FLOAT, 
                            [pre_amplitude] FLOAT, 
                            [after_price] FLOAT, 
                            [after_high_price] FLOAT, 
                            [after_low_price] FLOAT, 
                            [after_volume] INT, 
                            [after_turnover] FLOAT, 
                            [after_change_val] FLOAT, 
                            [after_change_rate] FLOAT, 
                            [after_amplitude] FLOAT) """  % self.stock_code
        self.exe_sql(sql_cmd_create,db='quote')

    def create_order_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  order_data_%s (
                            [code] TEXT,
                            [svr_recv_time_bid] CHAR,
                            [svr_recv_time_ask] CHAR,
                            [bid] TEXT,
                            [ask] TEXT) """  % self.stock_code
        self.exe_sql(sql_cmd_create,db='order')

    def save_data_tick(self,data_list):
        sql_cmd = """ replace into tick_data_%s(code,time,price,volume,turnover,ticker_direction,sequence,type,push_data_type) values(?,?,?,?,?,?,?,?,?) """ % self.stock_code
        insertItemList = []
        for row in data_list:
            insertItemList.append((row['code'],row['time'],row['price'],row['volume'],row['turnover'],row['ticker_direction'],row['sequence'],row['type'],row['push_data_type'] ))
        result = self.exe_sql_many(sql_cmd,insertItemList,db='tick')
        return result

    def save_data_rt(self,data_list):
        sql_cmd = """ replace into rt_data_%s(code,time,is_blank,opened_mins,cur_price,last_close,avg_price,turnover,volume,save_time) values(?,?,?,?,?,?,?,?,?,?) """ % self.stock_code
        insertItemList = []
        for row in data_list:
            insertItemList.append((row['code'],row['time'],row['is_blank'],row['opened_mins'],row['cur_price'],row['last_close'],row['avg_price'],row['turnover'],row['volume'],row['save_time'] ))
        result = self.exe_sql_many(sql_cmd,insertItemList,db='rt')
        return result

    def save_data_order(self,data_list):
        sql_cmd = """ insert into order_data_%s(code,svr_recv_time_bid,svr_recv_time_ask,bid,ask) values(?,?,?,?,?) """ % self.stock_code
        insertItemList = []
        for row in data_list:
            insertItemList.append((row['code'],row['svr_recv_time_bid'],row['svr_recv_time_ask'],json.dumps(row['Bid']),json.dumps(row['Ask'])))
        result = self.exe_sql_many(sql_cmd,insertItemList,db='order')
        return result

    def save_data_quote(self,data_list):
        filed_list = ['code','data_date','data_time','last_price','open_price','high_price','low_price','prev_close_price','volume','turnover','turnover_rate','amplitude','suspension','listing_date','price_spread','dark_status','sec_status','strike_price','contract_size','open_interest','implied_volatility','premium','delta','gamma','vega','theta','rho','net_open_interest','expiry_date_distance','contract_nominal_value','owner_lot_multiplier','option_area_type','contract_multiplier','pre_price','pre_high_price','pre_low_price','pre_volume','pre_turnover','pre_change_val','pre_change_rate','pre_amplitude','after_price','after_high_price','after_low_price','after_volume','after_turnover','after_change_val','after_change_rate','after_amplitude']
        sql_cmd = """ insert into quote_data_%s(""" % self.stock_code
        values = " values("
        for filed in filed_list:
            sql_cmd += "%s," % filed
            values += "?,"
        sql_cmd = sql_cmd[:-1]
        values  = values[:-1]
        sql_cmd = sql_cmd + ")" + values + ")"

        insertItemList = []
        for row in data_list:
            value_list = []
            for filed in filed_list:
                value_list.append(row[filed] if row[filed] != "N/A" else 0)
            insertItemList.append(value_list)
        result = self.exe_sql_many(sql_cmd,insertItemList,db='quote')
        return result

    def save_data_all(self,tab='tick',data_list=[]):
        if tab == "tick":
            self.save_data_tick(data_list)
        elif tab == "quote":
            self.save_data_quote(data_list)
        elif tab == "rt":
            self.save_data_rt(data_list)
        else:
            self.save_data_order(data_list)
        return True

    def save_queue_data(self,data_queue):
        last_time = time.time()
        now_time  = time.time()
        data_dict_list = {}
        while True:
            if data_queue.qsize() == 0:
                if now_time - last_time > 5 and len(data_dict_list[key]) > 0:
                    self.save_data_all(tab=key, data_list=data_dict_list[key])
                    last_time = now_time
                    print("[%s] save [%s] data length [%s]" % (key, self.stock_code, len(data_dict_list[key])))
                    data_dict_list[key] = []
                else:
                    time.sleep(3)
                    print("no data in queue,so sleep3 seconds")
                    now_time = time.time()
                    continue

            print("[%s] data_queue size is %s " % (self.stock_code,data_queue.qsize()))
            queue_data = data_queue.get()
            key = queue_data[0]
            if key not in data_dict_list:
                data_dict_list[key] = []
            data_dict_list[key].append(queue_data[1])

            for key in data_dict_list:
                if len(data_dict_list[key]) >= 10:
                    self.save_data_all(tab=key,data_list= data_dict_list[key])
                    last_time = now_time
                    print("[%s] save [%s] data length [%s]" % (key,self.stock_code,len(data_dict_list[key])))
                    data_dict_list[key] = []

            now_time = time.time()

        print("all finished")


def save_data(symbol,data_queue):
    stdObj = SavePushData(symbol)
    stdObj.create_tick_table()
    stdObj.create_rt_table()
    stdObj.create_quote_table()
    stdObj.create_order_table()
    stdObj.save_queue_data(data_queue)


class FutuDataSave(object):
    def __init__(self):
        self.quote_ctx = ft.OpenQuoteContext(host='127.0.0.1', port=11111)

        self.symbol_pools = ['HK.00700', 'HK.800000']
        # 获取top市值100的正股
        import filter_stock
        top_val_code_list = filter_stock.FilterStock(self.quote_ctx).get_hk_val_top(num=50)
        self.symbol_pools += top_val_code_list
        print("get top val code list is ", json.dumps(top_val_code_list, indent=4))
        top_turnover_code_list = filter_stock.FilterStock(self.quote_ctx).get_hk_turnover_rate_top(num=50)
        self.symbol_pools += top_turnover_code_list
        print("get top turnover code list is ", json.dumps(top_turnover_code_list, indent=4))
        sdi_obj = SaveDailyInfoData()
        sdi_obj.create_daily_info_table()
        sdi_obj.save_data_daily_info(top_val_code_list, top_turnover_code_list)

        # 获取最佳牛熊
        import mytool
        fsw_obj = mytool.FindStockWarrent(self.quote_ctx, "HK.800000")
        bear_list_800000, bull_list_800000 = fsw_obj.get_best_warrant()

        fsw_obj = mytool.FindStockWarrent(self.quote_ctx, "HK.00700")
        bear_list_00700, bull_list_00700 = fsw_obj.get_best_warrant()

        swd_obj = SaveWarrantData()
        swd_obj.create_warrant_table()
        swd_obj.save_data_warrant('800000', bull_list_800000, bear_list_800000)
        swd_obj.save_data_warrant('00700', bull_list_00700, bear_list_00700)
        
        self.data_queue_dict = {}
        for i in range(3):
            if bear_list_800000[i]:
                self.symbol_pools.append(bear_list_800000[i]['stock'])
            if bull_list_800000[i]:
                self.symbol_pools.append(bull_list_800000[i]['stock'])
            if bear_list_00700[i]:
                self.symbol_pools.append(bear_list_00700[i]['stock'])
            if bull_list_00700[i]:
                self.symbol_pools.append(bull_list_00700[i]['stock'])
        
        self.symbol_pools = list(set(self.symbol_pools))
        self.log("total symbol list length is %s" % len(self.symbol_pools))
        self.log("get symbol list is %s" % self.symbol_pools)

        for symbol in self.symbol_pools:
            self.data_queue_dict[symbol] = multiprocessing.Manager().Queue()

        class QuoteHandler(ft.StockQuoteHandlerBase):
            """报价处理器"""
            futu_data_event = self

            def on_recv_rsp(self, rsp_str):
                ret_code, content = super(QuoteHandler, self).on_recv_rsp(rsp_str)
                if ret_code != ft.RET_OK:
                    return ft.RET_ERROR, content
                self.futu_data_event.process_quote(content)
                return ft.RET_OK, content

        class OrderBookHandler(ft.OrderBookHandlerBase):
            """摆盘处理器"""
            futu_data_event = self

            def on_recv_rsp(self, rsp_str):
                ret_code, content = super(OrderBookHandler, self).on_recv_rsp(rsp_str)
                if ret_code != ft.RET_OK:
                    return ft.RET_ERROR, content
                self.futu_data_event.process_orderbook(content)
                return ft.RET_OK, content

        class TickerHandler(ft.TickerHandlerBase):
            """逐笔数据处理器"""
            futu_data_event = self

            def on_recv_rsp(self, rsp_str):
                ret_code, content = super(TickerHandler, self).on_recv_rsp(rsp_str)
                if ret_code != ft.RET_OK:
                    return ft.RET_ERROR, content
                self.futu_data_event.process_tick(content)
                return ft.RET_OK, content

        class RTDataHandler(ft.RTDataHandlerBase):
            """分时数据处理器"""
            futu_data_event = self

            def on_recv_rsp(self, rsp_str):
                ret_code, content = super(RTDataHandler, self).on_recv_rsp(rsp_str)
                if ret_code != ft.RET_OK:
                    return ft.RET_ERROR, content
                self.futu_data_event.process_rt(content)
                return ft.RET_OK, content

        class CurKlineHandler(ft.CurKlineHandlerBase):
            """实时k线推送处理器"""
            futu_data_event = self

            def on_recv_rsp(self, rsp_str):
                ret_code, content = super(CurKlineHandler, self).on_recv_rsp(rsp_str)
                if ret_code != ft.RET_OK:
                    return ft.RET_ERROR, content
                self.futu_data_event.process_curkline(content)
                return ft.RET_OK, content

        # 设置回调处理对象
        self.quote_ctx.set_handler(QuoteHandler())
        #self.quote_ctx.set_handler(OrderBookHandler())
        #self.quote_ctx.set_handler(CurKlineHandler())
        self.quote_ctx.set_handler(TickerHandler())
        self.quote_ctx.set_handler(RTDataHandler())

        # 定阅数据
        subtype_list = [ft.SubType.QUOTE, ft.SubType.ORDER_BOOK, ft.SubType.TICKER, ft.SubType.RT_DATA]
        ret, data = self.quote_ctx.subscribe(self.symbol_pools, subtype_list)
        if ret != ft.RET_OK:
            raise Exception('订阅行情失败：{}'.format(data))

    def run(self):
        for symbol in self.symbol_pools:
            p = multiprocessing.Process(target=save_data, args=(symbol, self.data_queue_dict[symbol]))
            p.start()
        p.join()

    def log(self,log_str):
        #print(log_str)
        pass

    def process_quote(self, data):
        """报价推送"""
        print("quote length is %s" % len(data))
        #print("quote data %s" % str(data))
        for ix, row in data.iterrows():
            tiny_quote = row.to_dict()
            self.log("quote data:" + json.dumps(tiny_quote, indent=4))
            self.data_queue_dict[tiny_quote['code']].put(["quote", tiny_quote])
        return True

    def process_tick(self, data):
        """tick推送"""
        print("tick length is %s" % len(data))
        for ix, row in data.iterrows():
            tiny_tick = row.to_dict()
            self.log("tick data:" + json.dumps(tiny_tick, indent=4))
            self.data_queue_dict[tiny_tick['code']].put(["tick", tiny_tick])
        return True

    def process_rt(self, data):
        """rt_data推送"""
        print("rt data length is %s" % len(data))
        for ix, row in data.iterrows():
            rt_data = row.to_dict()
            rt_data['save_time'] = time.time()
            self.log("rt data:" + json.dumps(rt_data, indent=4))
            self.data_queue_dict[rt_data['code']].put(["rt", rt_data])
        return True

    def process_orderbook(self, data):
        """订单簿推送"""
        #print("order book %s" % str(data))
        self.data_queue_dict[data['code']].put(["order", data])
        return True


if __name__ =="__main__":
    ft.set_futu_debug_model(True)
    ''' 行情api测试 '''
    fds_obj = FutuDataSave()
    fds_obj.run()
    print("finished")




