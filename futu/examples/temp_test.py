from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

req = WarrantRequest()
req.sort_field = SortField.TURNOVER
# req.type_list = WrtType.CALL
# req.cur_price_min = 0.1
# req.cur_price_max = 0.2
req.begin = 100
req.num = 100
ret, ls = quote_ctx.get_warrant("HK.800000", req)
if ret == RET_OK:  # 先判断接口返回是否正常，再取数据
    warrant_data_list, last_page, all_count = ls
    print(len(warrant_data_list), last_page, all_count)   
else:
    print('error: ', ls)

quote_ctx.close() 