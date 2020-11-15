# 15.logging
import logging

# 基本用法
# 使用baseConfig()来指定日志输出级别
# 默认情况下是追加到log
# basicConfig(filemode='w') filename level
# logging.basicConfig(filename='demo.log',level=logging.DEBUG)
# 默认是warning （后三种）
# logging.debug("This is debug log") # 调试
# logging.info("This is info log") # 信息
# logging.warning("This is warning log") # 提示
# logging.error("This is error log")#错误
# logging.critical("This is critical log")#崩溃

# 输出字符串
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('姓名{0} 年龄{1}'.format('叶毓琇',18))

# 输出格式和添加一些公共信息
# 时间 等级名字 文件名 第几行 信息
# logging.basicConfig(format="%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s",level=logging.DEBUG,
#                     datefmt="%Y-%m-%d %H:%M:%S")
# logging.debug('姓名{0} 年龄{1}'.format('叶毓琇',18))
# logging.warning('姓名{0} 年龄{1}'.format('叶毓琇',11))

# logging高级用法
'''
Loggers : 记录器
    1. 提供应用成功徐调用接口
    logger = logging.getLogger(__name__)
    2. 决定日志记录的级别
    logger.setLevel()
    3. 将日志内容传递到相关联的 handlers 中
    logger.addHandler() logger.removeHandler()
Handlers : 处理器( StreamHandler \ FileHandler \ BaseRotatingHandler \ TimedRotatingFileHandler \
 SocketHandler \ DatagramHandler \ SMTPHandler SysLogHandler ..)
将日志分别发到不同目的地，文件 console 邮件 通过http到任何地方
    1. StreamHandler
    标准输出 stdout(显示器)
    创建方法 sh = logging.StreamHandler(stream = None)
    2. FileHandler
    将日志保存到磁盘文件
    创建方法 fh = logging.FileHandler(filename , mode='a',encoding= None, delay=False)
    setFormatter(): 设置当前handler对象使用的消息格式

Filters : 过滤器
Formatters : 格式化器
用来最终设置日志信息的顺序结构和内容
ft = loggign.Formatter.__init__(fmt=None,datefmt=None,style=None)
'''
# 代码形式打印日志


# 记录器（笔）
# 设置的是名字
# logger = logging.getLogger('test.log')
# logger.setLevel(logging.DEBUG)
#
# # 处理器（往哪里去写）
# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.DEBUG)
#
# # fileHandler = logging.FileHandler(filename='demo.log',)
#
# # formatter格式
# formatter = logging.Formatter("%(asctime)s|%(levelname)8s|%(filename)s:%(lineno)s|%(message)s")
# # 设置格式
# consoleHandler.setFormatter(formatter)
# # fileHandler.setFormatter(formatter)
#
# # 记录器要设置处理器
# logger.addHandler(consoleHandler)
# # logger.addHandler(fileHandler)
#
# # 定义一个过滤器
# flt = logging.Filter("test.log")
#
# logger.addFilter(flt)
# # 打印日志的代码(对象不同了)
# logger.debug('姓名{0} 年龄{1}'.format('叶毓琇',18))
# logger.warning('姓名{0} 年龄{1}'.format('叶毓琇',18))
# logger.info('姓名{0} 年龄{1}'.format('叶毓琇',18))
# logger.error('姓名{0} 年龄{1}'.format('叶毓琇',18))
# logger.critical('姓名{0} 年龄{1}'.format('叶毓琇',18))

# Formatters 格式
'''
%(asctime)s  日志产生时间 默认 Y-m-d H:M:s ,毫秒 用 datafmt= "%Y-%m-%d"改变
%(created)f  time.time()生成的日志创建时间截
%(filename)s 生成日志的程序文件名
%(funcName)s 调用日志的函数名
%(levelname)s 日志级别
%(levelno)s 日志级别对应的数值
%(lineno)s 日志所在的代码行号
%(module)s 生成日志的模块名
%(msecs)s 日志生成时间的毫秒部分
%(message)s 日志信息
%(name)s 日志调用者
%(pathname)s 生成日志的文件的完整路径
%(process)d 生成日志的进程ID
%(processName)s 进程名
%(thread)d 线程iD
%(threadName)s  线程名



'''