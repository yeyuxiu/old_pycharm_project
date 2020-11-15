'''
mitmdump -p 8888 -s filename.py
在安卓模拟器中配置wifi 并  上网就可以打印日志版得请求头信息

'''

from mitmproxy import ctx

# 必须这么写

def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))
    ctx.log.warn(str(flow.request.headers))
    ctx.log.error(str(flow.request.headers))
