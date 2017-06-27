#-*-coding=utf-8-*-
__author__ = 'vigar'

import tushare as ts
import os
import time

info=ts.get_stock_basics()

def loop_all_stocks():
    count=0
    for stockId in info.index:
        filename = 'E:/stock/tushare_code/allcsv_k/'+stockId+'.csv'
        count=count+1
        if os.path.exists(filename):
            message="file exist! no need to download"
        else:
                try:
                        #df = ts.get_hist_data(stockId)
                        df = ts.get_k_data(stockId)
                        df.to_csv(filename)
                        message="download file " + filename + " success!"
                except Exception,e:
                        traceback.print_exc()
                        log_error(stockId)
                        message="download file " + filename + " fail!"

        print "[" + str(count) + "] " + message
        time.sleep(1)


def log_error(info):
    f = open('E:/stock/tushare_code/fail.csv', 'a')
    f.write(info+"\n")
    f.close()

loop_all_stocks()
