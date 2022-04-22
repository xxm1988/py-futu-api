from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

# req = WarrantRequest()
# req.sort_field = SortField.TURNOVER
# req.type_list = WrtType.CALL
# req.cur_price_min = 0.1
# req.cur_price_max = 0.2
# ret, ls = quote_ctx.get_warrant("HK.00700", req)
# if ret == RET_OK:  # 先判断接口返回是否正常，再取数据
#     warrant_data_list, last_page, all_count = ls
#     print(len(warrant_data_list), all_count, warrant_data_list)
#     print(warrant_data_list['stock'][0])    # 取第一条的窝轮代码
#     print(warrant_data_list['stock'].values.tolist())   # 转为 list
# else:
#     print('error: ', ls)
    
req = WarrantRequest()
req.begin = 0
req.num = 100
req.sort_field = SortField.TURNOVER
#req.issuer_list = ['UB','CS','BI']
req.ascend = True
req.status = WarrantStatus.NORMAL  # Qot_Common.WarrantStatus, 窝轮状态
req.street_min = 5       # 街货占比 % 过滤起点
req.vol_min    = 1000    # 成交量过滤起点
req.maturity_time_min = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")  # 到期日, 到期日范围的开始时间戳
req.maturity_time_max = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
req.type_list = [WrtType.BULL, ]    # Qot_Common.WarrantType, 窝轮类型过滤列表 WrtType        
req.price_recovery_ratio_min = -20    # 正股距回收价 % 过滤起点, 仅牛熊证支持该字段过滤
req.price_recovery_ratio_max = 20  # 正股距回收价 % 过滤终点, 仅牛熊证支持该字段过滤

ret, ls = quote_ctx.get_warrant(Market.HK, req)
if ret == RET_OK: 
    warrant_data_list, last_page, all_count = ls
    print("length", len(warrant_data_list))
    print("all count:" , all_count)
    print(warrant_data_list)
else:
    print('error: ', ls)

quote_ctx.close()  # 所有接口结尾加上这条 close，防止连接条数用尽