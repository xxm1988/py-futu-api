# -*- coding: utf-8 -*-

# 导入futu-api
import futu as ft

import pandas as pd
pd.set_option('display.width',2000)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.max_columns',100)


# 实例化行情上下文对象
quote_ctx = ft.OpenQuoteContext(host="100.66.37.76", port=8080)

# 上下文控制
quote_ctx.start()              # 开启异步数据接收
quote_ctx.set_handler(ft.TickerHandlerBase())  # 设置用于异步处理数据的回调对象(可派生支持自定义)

# 低频数据接口
market = ft.Market.HK
code = 'HK.800000'
code_list = [code]

# print(quote_ctx.get_trading_days(market, start=None, end=None))                # 获取交易日
# print(quote_ctx.get_stock_basicinfo(market, stock_type=ft.SecurityType.IDX))   # 获取股票信息


# # 高频数据接口
#quote_ctx.subscribe(code, [ft.SubType.TICKER, ft.SubType.K_DAY, ft.SubType.RT_DATA])
#quote_ctx.subscribe(code, [ft.SubType.QUOTE, ft.SubType.TICKER, ft.SubType.K_DAY, ft.SubType.ORDER_BOOK, ft.SubType.RT_DATA, ft.SubType.BROKER])
# print(quote_ctx.get_stock_quote(code))      # 获取报价
# print(quote_ctx.get_rt_ticker(code))        # 获取逐笔
# print(quote_ctx.get_cur_kline(code, num=100, ktype=ft.KLType.K_DAY))   #获取当前K线
# print(quote_ctx.get_order_book(code))       # 获取摆盘

#ret_code,result = quote_ctx.get_rt_data(code)

# import pprint
# pp = pprint.PrettyPrinter(indent=4,width=500)
# pp.pprint(quote_ctx.get_referencestock_list(code, ft.SecurityReferenceType.WARRANT))

ret ,result = quote_ctx.get_referencestock_list(code, ft.SecurityReferenceType.WARRANT)
import sys
for index, row in result.iterrows():
    print(row["code"], row["stock_name"])
    sys.exit()

for row in result.itertuples():
    print(row)
    print(row['code'])
    sys.exit()

# import pdb
# pdb.set_trace()

# result.to_csv("C:\\Users\\encorexiao\\Desktop\\800000.csv")
#
#
# print(result)          # 获取分时数据
# print(quote_ctx.get_broker_queue(code))     # 获取经纪队列