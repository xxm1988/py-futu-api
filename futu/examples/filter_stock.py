from futu import *
import time

class FilterStock():
    def __init__(self, quote_ctx):
        self.quote_ctx = quote_ctx

    def get_hk_val_top(self, num=200):
        simple_filter = SimpleFilter()
        simple_filter.filter_min = 200 * 10000 * 10000
        simple_filter.filter_max = 100000 * 10000 * 10000
        simple_filter.stock_field = StockField.MARKET_VAL
        #simple_filter.stock_field = StockField.CUR_PRICE
        simple_filter.is_no_filter = False
        simple_filter.sort = SortDir.DESCEND
        code_list = []
        ret, ls = self.quote_ctx.get_stock_filter(market=Market.HK, filter_list=[simple_filter,], begin=0 ,num=num)  # 对香港市场的股票做简单、财务和指标筛选
        if ret == RET_OK:
            last_page, all_count, ret_list = ls
            print('all count = ', all_count)
            print('last_page = ', last_page)
            for item in ret_list:             
                #print(item)   
                code_list.append(item.stock_code)
                print(f"{item.stock_code}\t\t{item.stock_name}\t\t{item.market_val}")               
        else:
            print('error: ', ls)
        
        return code_list

        
if __name__ == "__main__":
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    fs_obj = FilterStock(quote_ctx)
    code_list = fs_obj.get_hk_val_top()
    print(code_list)
    quote_ctx.close()  # 结束后记得关闭当条连接，防止连接条数用尽
 