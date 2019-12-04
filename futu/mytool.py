# -*- coding: utf-8 -*-

# 导入futu-api
import futu as ft

import pandas as pd
pd.set_option('display.width',2000)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.max_columns',100)

class FindStockWarrent():
    def __init__(self,quote_ctx,stock_code):
        self.code   = stock_code
        self.market = ft.Market.HK
        # 行情上下文对象
        self.quote_ctx = quote_ctx

    def get_stock_refer_warrant(self):
        ret ,result = self.quote_ctx.get_referencestock_list(self.code, ft.SecurityReferenceType.WARRANT)
        if not ret:
            return False,[]
        warrant_list = []
        for index, row in result.iterrows():
            warrant_list.append(row["code"])
        return True,warrant_list


    def get_best_warrant(self,recovery_rate_min,recovery_rate_max,wrt_type=0):
        # wrt_type 0  BULL 1 BEAR
        ret,warrant_list = self.get_stock_refer_warrant()
        if not ret:
            return False,[]

        ret,result = self.quote_ctx.get_market_snapshot(warrant_list)
        if not ret:
            return False

        best_list = []
        for index, row in result.iterrows():
            best_list.append(row["code"],row["last_price"],row["last_price"],row["volume"],row["turnover"],row["last_price"],row["last_price"],row["last_price"],row["last_price"],row["last_price"],row["last_price"],row["last_price"],row["last_price"],row["last_price"])


if __name__ == "__main__":
    fsw_obj = FindStockWarrent()