#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from  datetime import datetime
#
#@param g  数据库连接对象
#@param 表名 
#
#
#

def select(g,*wargs,**kwargs):
    pass


def time_format(time_str):
    #将时间字符串转换为时间邮戳
    time_tuple = time.strptime(time_str,'%Y/%m/%d %H:%M:%S')

    #按照指定的格式格式化时间邮戳
    return time.strftime("%Y-%m-%d %H:%M:%S",time_tuple)

if __name__ == '__main__':
    print time_format('2012/12/5 2:45:14')