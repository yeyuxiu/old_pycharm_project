# 与时间处理相关的模块 : time , datetime , calendar

"""
时间戳（timestamp）的方式：通常来说，时间戳表示的是从 1970 年 1 月 1 日 00:00:00 开始按秒计算的偏移量（time.gmtime(0)）此模块中的函数无法处理 1970 纪元年以前的日期和时间或太遥远的未来（处理极限取决于 C 函数库，对于 32 位系统来说，是 2038 年）
UTC（Coordinated Universal Time，世界协调时）也叫格林威治天文时间，是世界标准时间。在中国为 UTC+8
DST（Daylight Saving Time）即夏令时的意思
一些实时函数的计算精度可能低于它们建议的值或参数，例如在大部分 Unix 系统，时钟一秒钟“滴答”50~100 次
"""

import time as t
# time.struct_time(tm_year=2014, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=334, tm_isdst=-1)
type(t.localtime()) # <class 'time.struct_time'> 时间元组 上面就是时间元组
# tm_wday(星期几) tm_yday(一年中的第几天)0表示星期一 tm_isdst(是否为夏令时)-1代表夏令时
t.localtime() # 返回当地时间
t.asctime(t.localtime()) # Sat Jul 18 09:53:26 2020
t.perf_counter() # 返回系统运行时间
t.process_time() # 返回进程运行时间
t.ctime() # 未给参数等于 t.asctime(t.localtime())
t.gmtime() # 接收时间辍并返回格林威治天文时间下的时间元组 t
t.localtime() # 接受时间截返回当地时间下的时间元组
t.mktime(t.localtime()) # 接受时间元组并返回时间截
# t.sleep()
t.strftime("%a, %d %b %Y %H:%M:%S +0000",t.localtime()) #
# Sat, 18 Jul 2020 10:12:07 +0000
t.strptime("30 Nov 14", "%d %b %y") # 把一个格式化时间字符串转化为 struct_time。实际上它和 strftime() 是逆操作。
# time.struct_time(tm_year=2014, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=334, tm_isdst=-1)

t.time() # 返回当前时间截



