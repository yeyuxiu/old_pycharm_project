'''
在配置文件中，首先包含了三大主要模块，loggers, handlers, formatters。对于三个主要模块其包含的内容都是通过keys进行指定，
然后通过logger_ke/handler_key/formatter_key对里面的key进行具体的设置。
loggers配置logger的模块，其中必须包含一个名字叫做root的logger，当在应用程序中，
使用无参函数logging.getLogger()时，默认返回root这个logger，其他自定义logger可以通过 logging.getLogger("name") 方式进行调用。
handlers定义handlers的信息，通过keys进行指定。里面可以指定我们日志的输出方式、日志的级别、日志的格式等。
formatters表示设置日志的格式。
logger-XXX对loggers中声明的logger进行逐个配置，且要一一对应,在所有的logger中，必须制定lebel和handlers这两个选项，
对于非roothandler，还需要添加一些额外的option，其中qualname表示它在logger层级中的名字，在应用代码中通过这个名字制定所使用的handler，
即 logging.getLogger("fileAndConsole")，handlers可以指定多个，中间用逗号隔开，比如handlers=fileHandler,consoleHandler，
同时制定使用控制台和文件输出日志。propagate通常设为零，这样，当我们在handlers中设置多个处理器时，不会多次打印日志信息。
handler_xxx在handler中，必须指定class和args这两个option，
常用的class包括 StreamHandler（仅将日志输出到控制台）、FileHandler（将日志信息输出保存到文件）、
RotaRotatingFileHandler（将日志输出保存到文件中，并设置单个日志wenj文件的大小和日志文件个数），
args表示传递给class所指定的handler类初始化方法参数，它必须是一个元组（tuple）的形式，
即便只有一个参数值也需要是一个元组的形式；里面指定输出路径，比如输出的文件名称等。level与logger中的level一样，
而formatter指定的是该处理器所使用的格式器，这里指定的格式器名称必须出现在formatters这个section中，
且在配置文件中必须要有这个formatter的section定义；如果不指定formatter则该handler将会以消息本身作为日志消息进行记录，而不添加额外的时间、日志器名称等信息；
在这个配置文件中设置了三种日志的输出方式，root对应控制台输出、file对应配置文件输出、fileAndConsole对应着文件和控制台同时输出
'''
# 配置文件形式打印日志
import logging.config

# '读取日志配置文件'
logging.config.fileConfig('logging.conf')

# 创建一个日志器logger
logger = logging.getLogger('fileAndConsole')
logger.debug('debug')
logger.info('info')
logger.warning('warn')
logger.error('error')
logger.critical('critical')