#-*-coding=utf-8-*-
__author__ = 'vigar'

import tushare as ts
import os

filename = 'E:/stock/tushare_code/basicinfo.xlsx'
basic = ts.get_stock_basics()
#basic.to_csv(filename)
basic.to_excel(filename)
