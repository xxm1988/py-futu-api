# encoding: UTF-8

'''
    实盘策略范例，接口用法见注释及范例代码
'''
import talib
import sqlite3
import platform
import multiprocessing
from sqlalchemy import create_engine
from futu.examples.tiny_quant.tiny_quant_frame.TinyQuantFrame import *
from futu.examples.tiny_quant.tiny_quant_frame.TinyStrateBase import *

class SaveTickData():
    def __init__(self,stock_code,data_date=None):
        self.stock_code  = stock_code.split('.')[1]
        if data_date:
            self.data_date = data_date
        else:
            self.data_date = datetime.now().strftime('%Y%m%d')

        if platform.system() == "Windows":
            self.sqlitedb_order = sqlite3.connect(u"D:\\StockData\\stock_order.db")
            self.sqlitedb_tick  = sqlite3.connect(u"D:\\StockData\\stock_tick.db")
            self.sqlitedb_quote = sqlite3.connect(u"D:\\StockData\\stock_quote.db")
            self.sqlitedb_rt    = sqlite3.connect(u"D:\\StockData\\stock_rt.db")
            self.sqlitedb_war   = sqlite3.connect(u"D:\\StockData\\stock_warrant.db")
        else:
            self.sqlitedb_order = sqlite3.connect(u"/data/ft_hist_data/tick_data/stock_order.db")
            self.sqlitedb_tick  = sqlite3.connect(u"/data/ft_hist_data/tick_data/stock_tick.db")
            self.sqlitedb_quote = sqlite3.connect(u"/data/ft_hist_data/tick_data/stock_quote.db")
            self.sqlitedb_rt    = sqlite3.connect(u"/data/ft_hist_data/tick_data/stock_rt.db")
            self.sqlitedb_war   = sqlite3.connect(u"/data/ft_hist_data/tick_data/stock_warrant.db")

    def __del__(self):
        self.sqlitedb_order.close()
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

    def create_warrant_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  stock_ref_warrant (
                            [code] TEXT,
                            [date] DATE,
                            [bull_1] TEXT,
                            [bull_2] TEXT,
                            [bull_3] TEXT,
                            [bear_1] TEXT,
                            [bear_2] TEXT,
                            [bear_3] TEXT,
                            PRIMARY KEY([code], [date])) """
        self.exe_sql(sql_cmd_create,db='war')

    def create_tick_table(self):
        sql_cmd_create = """create TABLE IF NOT EXISTS  tick_data_%s (
                            [code] TEXT,
                            [time] DATETIME,
                            [price] FLOAT,
                            [volume] FLOAT,
                            [turnover] FLOAT,
                            [ticker_direction] TEXT,
                            [sequence] REAL,
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
                            [volume] FLOAT) """  % self.stock_code
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

    def save_data_warrant(self,bull_list,bear_list):
        sql_cmd = """ replace into stock_ref_warrant(code,date,bull_1,bull_2,bull_3,bear_1,bear_2,bear_3) 
                      values('%s','%s','%s','%s','%s','%s','%s','%s') 
                  """ % (self.stock_code,datetime.now().strftime('%Y-%m-%d'),bull_list[0],bull_list[1],bull_list[2],bear_list[0],bear_list[1],bear_list[2])
        result = self.exe_sql(sql_cmd,db='war')
        return result

    def save_data_tick(self,data_list):
        sql_cmd = """ replace into tick_data_%s(code,time,price,volume,turnover,ticker_direction,sequence,type,push_data_type) values(?,?,?,?,?,?,?,?,?) """ % self.stock_code
        insertItemList = []
        for row in data_list:
            insertItemList.append((row['code'],row['time'],row['price'],row['volume'],row['turnover'],row['ticker_direction'],row['sequence'],row['type'],row['push_data_type'] ))
        result = self.exe_sql_many(sql_cmd,insertItemList,db='tick')
        return result

    def save_data_rt(self,data_list):
        sql_cmd = """ replace into rt_data_%s(code,time,is_blank,opened_mins,cur_price,last_close,avg_price,turnover,volume) values(?,?,?,?,?,?,?,?,?) """ % self.stock_code
        insertItemList = []
        for row in data_list:
            insertItemList.append((row['code'],row['time'],row['is_blank'],row['opened_mins'],row['cur_price'],row['last_close'],row['avg_price'],row['turnover'],row['volume'] ))
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
                time.sleep(3)
                #print("no data in queue,so sleep3 seconds")
                continue

            #print("[%s] data_queue size is %s " % (symbol,data_queue.qsize()))
            queue_data = data_queue.get()
            key = queue_data[0]
            if key not in data_dict_list:
                data_dict_list[key] = []
            data_dict_list[key].append(queue_data[1])

            for key in data_dict_list:
                if len(data_dict_list[key]) > 10:
                    self.save_data_all(tab=key,data_list= data_dict_list[key])
                    save_flag = True
                    last_time = now_time
                    print("[%s] save [%s] data length [%s]" % (key,self.stock_code,len(data_dict_list[key])))
                    data_dict_list[key] = []
                elif now_time - last_time > 5 and len(data_dict_list[key]) > 0:
                    self.save_data_all(tab=key, data_list=data_dict_list[key])
                    save_flag = True
                    last_time = now_time
                    print("[%s] save [%s] data length [%s]" % (key,self.stock_code,len(data_dict_list[key])))
                    data_dict_list[key] = []
                else:
                    pass

            now_time = time.time()
            save_flag = False

        print("all finished")

def save_data(symbol,data_queue):
    stdObj = SaveTickData(symbol)
    stdObj.create_tick_table()
    stdObj.create_rt_table()
    stdObj.create_quote_table()
    stdObj.create_order_table()
    stdObj.save_queue_data(data_queue)

class TinyStrateSaveTick(TinyStrateBase):
    """策略名称, setting.json中作为该策略配置的key"""
    name = 'tiny_strate_save_tick'

    """策略需要用到行情数据的股票池"""
    symbol_pools = ['HK.00700']
    symbol_pools = ['HK.800000']

    def __init__(self):
        super(TinyStrateSaveTick, self).__init__()

        """请在setting.json中配置参数"""
        self.param1 = None
        self.param2 = None
        self.data_queue_dict = {}

    def on_init_strate(self):
        """策略加载完配置后的回调
        1. 可修改symbol_pools 或策略内部其它变量的初始化
        2. 此时还不能调用futu api的接口
        """
        self.log("begin to init strate")
        from futu import OpenQuoteContext,mytool
        quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
        fsw_obj   = mytool.FindStockWarrent(quote_ctx, "HK.800000")
        bear_list_800000, bull_list_800000 = fsw_obj.get_best_warrant()

        fsw_obj = mytool.FindStockWarrent(quote_ctx, "HK.00700")
        bear_list_00700, bull_list_00700 = fsw_obj.get_best_warrant()

        std_obj = SaveTickData(stock_code="HK.800000")
        std_obj.create_warrant_table()
        std_obj.save_data_warrant(bull_list_800000,bear_list_800000)

        std_obj = SaveTickData(stock_code="HK.00700")
        std_obj.create_warrant_table()
        std_obj.save_data_warrant(bull_list_00700, bear_list_00700)

        TinyStrateSaveTick.symbol_pools = ['HK.00700','HK.800000']
        for i in range(3):
            if bear_list_800000[i]:
                TinyStrateSaveTick.symbol_pools.append(json.loads(bear_list_800000[i])['stock'])
            if bull_list_800000[i]:
                TinyStrateSaveTick.symbol_pools.append(json.loads(bull_list_800000[i])['stock'])
            if bear_list_00700[i]:
                TinyStrateSaveTick.symbol_pools.append(json.loads(bear_list_00700[i])['stock'])
            if bull_list_00700[i]:
                TinyStrateSaveTick.symbol_pools.append(json.loads(bull_list_00700[i])['stock'])
        self.log("get symbol list is %s" % TinyStrateSaveTick.symbol_pools)
        for symbol in TinyStrateSaveTick.symbol_pools:
            self.data_queue_dict[symbol] = multiprocessing.Manager().Queue()
            p = multiprocessing.Process(target=save_data,args=(symbol,self.data_queue_dict[symbol]))
            p.start()

    def on_start(self):
        """策略启动完成后的回调
        1. 框架已经完成初始化， 可调用任意的futu api接口
        2. 修改symbol_pools无效, 不会有动态的行情数据回调
        """
        self.log("on_start param1=%s param2=%s" %(self.param1, self.param2))

        """交易接口测试
        ret, data = self.buy(4.60, 1000, 'HK.03883')
        if 0 == ret:
            order_id = data
            ret, data = self.get_tiny_trade_order(order_id)
            if 0 == ret:
                str_info = ''
                for key in data.__dict__.keys():
                    str_info += "%s='%s' " % (key, data.__dict__[key])
                print str_info

        ret, data = self.sell(11.4, 1000, 'HK.01357')
        if 0 == ret:
            order_id = data
            self.cancel_order(order_id)
        """

    def on_tick_changed(self, tiny_tick):
        """tick变化时，会触发该回调"""
        #print(tiny_tick)
        #self.log("tick data:"+json.dumps(tiny_tick,indent=4))
        self.data_queue_dict[tiny_tick['code']].put(["tick", tiny_tick])
        return True

    def on_rt_changed(self, rt_data):
        """分时变化时，会触发该回调"""
        #print(rt_data)
        #self.log("rt data:"+json.dumps(rt_data,indent=4))
        self.data_queue_dict[rt_data['code']].put(["rt", rt_data])
        return True

    def on_quote_changed(self, tiny_quote):
        """报价实时数据变化时，会触发该回调"""
        #print(tiny_quote)
        #self.log("quote data:"+json.dumps(tiny_quote,indent=4))
        self.data_queue_dict[tiny_quote['code']].put(["quote", tiny_quote])
        return True

    def on_order_book(self, order_book):
        """摆盘实时数据变化时，会触发该回调"""
        #print(order_book)
        #self.log("order book:"+json.dumps(order_book,indent=4))
        self.data_queue_dict[order_book['code']].put(["order", order_book])
        return True

    def on_bar_min1(self, tiny_bar):
        """每一分钟触发一次回调"""
        bar = tiny_bar
        symbol = bar.symbol
        str_dt = bar.datetime.strftime("%Y%m%d %H:%M:%S")

        # 得到分k数据的ArrayManager(vnpy)对象
        am = self.get_kl_min1_am(symbol)
        array_high = am.high
        array_low = am.low
        array_open = am.open
        array_close = am.close
        array_vol = am.volume

        n = 5
        ma_high = self.ema(array_high, n)
        ma_low = self.ema(array_low, n)
        ma_open = self.ema(array_open, n)
        ma_close = self.ema(array_close, n)
        ma_vol = self.ema(array_vol, n)

        str_log = "on_bar_min1 symbol=%s dt=%s ema(%s) open=%s high=%s close=%s low=%s vol=%s" % (
            symbol, str_dt, n, ma_open, ma_high, ma_close, ma_low, ma_vol)
        #self.log(str_log)

    def on_bar_day(self, tiny_bar):
        """收盘时会触发一次日k回调"""
        bar = tiny_bar
        symbol = bar.symbol
        str_dt = bar.datetime.strftime("%Y%m%d %H:%M:%S")
        str_log = "on_bar_day symbol=%s dt=%s  open=%s high=%s close=%s low=%s vol=%s" % (
            symbol, str_dt, bar.open, bar.high, bar.close, bar.low, bar.volume)
        self.log(str_log)

    def on_before_trading(self, date_time):
        """开盘时触发一次回调, 脚本挂机切换交易日时，港股会在09:30:00回调"""
        str_log = "on_before_trading - %s" % date_time.strftime('%Y-%m-%d %H:%M:%S')
        self.log(str_log)

    def on_after_trading(self, date_time):
        """收盘时触发一次回调, 脚本挂机时，港股会在16:00:00回调"""
        str_log = "on_after_trading - %s" % date_time.strftime('%Y-%m-%d %H:%M:%S')
        self.log(str_log)
        import sys
        sys.exit()

    def sma(self, np_array, n, array=False):
        """简单均线"""
        if n < 2:
            result = np_array
        else:
            result = talib.SMA(np_array, n)
        if array:
            return result
        return result[-1]

    def ema(self, np_array, n, array=False):
        """移动均线"""
        if n < 2:
            result = np_array
        else:
            result = talib.EMA(np_array, n)
        if array:
            return result
        return result[-1]


if __name__ == '__main__':
    my_strate = TinyStrateSaveTick()
    frame = TinyQuantFrame(my_strate)
    frame.run()
    frame.stop()

