# -*- coding: utf-8 -*-

# 导入futu-api
from futu import *
import pandas as pd
#from datetime import timedelta
from futu.quote.quote_get_warrant import Request

pd.set_option('display.width',2000)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.max_columns',100)

class FindStockWarrent():
    def __init__(self,quote_ctx,stock_code):
        self.stock_code = stock_code
        self.quote_ctx  = quote_ctx

    def get_warrant(self,recovery_rate_min=1,recovery_rate_max=5,wrt_type="bull"):
        req = Request()
        req.sort_field = SortField.SCORE
        req.ascend = False
        req.status = WarrantStatus.NORMAL  # Qot_Common.WarrantStatus, 窝轮状态
        req.street_min = 10     # 街货占比 % 过滤起点
        #req.vol_min    = 1000   # 成交量过滤起点
        req.premium_min = None  # 溢价 % 过滤起点
        req.maturity_time_min = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")  # 到期日, 到期日范围的开始时间戳
        if wrt_type == "bull":
            req.type_list = [WrtType.BULL, ]  # Qot_Common.WarrantType, 窝轮类型过滤列表 WrtType
        else:
            req.type_list = [WrtType.BEAR,]  # Qot_Common.WarrantType, 窝轮类型过滤列表 WrtType
        #req.issuer_list = [Issuer.CS, Issuer.CT, Issuer.EA]  # Qot_Common.Issuer, 发行人过滤列表
        req.price_recovery_ratio_min = recovery_rate_min  # 正股距回收价 % 过滤起点, 仅牛熊证支持该字段过滤
        req.price_recovery_ratio_max = recovery_rate_max  # 正股距回收价 % 过滤终点, 仅牛熊证支持该字段过滤

        return  self.quote_ctx.get_warrant(self.stock_code, req)

    def get_best_warrant(self):
        ret = self.get_warrant(recovery_rate_min=-5, recovery_rate_max=-1, wrt_type='bear')
        bear_list = []
        bull_list = []
        if ret[0] == RET_OK:
            for index, rows in ret[1][0].iterrows():
                if len(bear_list) >= 5:
                    break
                bear_list.append(json.dumps(rows.to_dict()))
        else:
            return [],[]
        ret = self.get_warrant(recovery_rate_min=1, recovery_rate_max=5, wrt_type='bull')
        bull_list = []
        if ret[0] == RET_OK:
            for index, rows in ret[1][0].iterrows():
                if len(bull_list) >= 5:
                    break
                bull_list.append(json.dumps(rows.to_dict()))
        else:
            return bear_list,[]
        # 最后再加三个空，防止总数少于三个拿不到三个
        bear_list += [{},{},{}]
        bull_list += [{},{},{}]
        return bear_list,bull_list


if __name__ == "__main__":
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    # req = Request()
    # print(quote_ctx.get_warrant('HK.800000', req))

    fsw_obj = FindStockWarrent(quote_ctx,"HK.800000")
    bear_list,bull_list = fsw_obj.get_best_warrant()
    print(len(bear_list))
    print(len(bull_list))
    print(bear_list)
    print(bull_list)