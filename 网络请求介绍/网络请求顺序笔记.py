# 网络请求顺序
# 完整的网络请求过程
'''
输入网址 -> 传输到浏览器 -> 浏览器向DNS服务器查找ip -> 查找到ip浏览器向web服务器建立TCP连接
同时发起http请求->最后web服务器返回 html到浏览器(浏览器做渲染加载js文档等)
'''
# IP地址 和 url
'''
1. IP地址
    互联网只认识ip地址，所有的网络请求到数据传输底层都是ip地址
    动态ip
       IP地址:192.168开头都是本地局域网ip地址（内部ip，访问网站是{百度搜本机ip的ip}）
       且当用户关闭路由器的时候，这个ip就会给其他人用 
    静态ip
        ip一直都是这个，这种就适合做服务器
2. url
    统一资源定位符，可以指向一个html，js，css，图片，文件
3. url协议
    http : // www.baidu.com :80 / path / my.html?key=1 # maodian
    http:// 协议
    www.baidu.com 域名 (方便记住)
    :80 端口 指明服务器上哪个应用
    /path/my.html 路径 (访问具体的页面) (类似于函数)
    ?key=1 在具体页面的基础上传递参数 (类似于传参)
    # maodian 锚点 在同一页面的具体位置 (在百度百科搜朱元璋点击目录)
4.常用协议
    http , https , file , ftp
    相对url
    平时看见的 href里面的url，缺少域名
    绝对url
    带有域名的完整url
5. 计算机常见的网络协议(从上而下)
    应用层 Http、ftp、pop3、DNS
    传输层 TCP、UDP
    网络层 ICMP、IP、IGMP
    数据链路层 ARP、RARP
    物理层 物理传输介质
    
    传输过程 (浏览器访问服务器)
    浏览器(应用层) -> 数据传输(传输层) -> 路由器(网络层) -> 交换机(数据链路层) ->双绞线/集线器(物理层)
    (服务器返回浏览器)
    反过来
    服务器开发 一般了解socket编程即可
6. IP/TCP 协议功能
    ip协议负责将元IP地址 跟 目标ip地址连接起来 进行数据传输
    
    TCP协议将数据分成等分片段
'''

# 前端基础

# html、css、js 之间的关系
'''
html 是骨骼 css 是皮肤 js 是肌肉
'''
# 浏览器加载过程
'''
构建dom树
字资源加载- 加载外部的css 图片 js
样式渲染 - css执行
'''
# AJAX
'''
AJAX 是一种用用于创建快速动态网页的技术
json 和 xml 的产生需求:
    跨语言的数据格式
'''
# 三种 content-type 方式
'''
1.application/x-js/www-form-urlencoded
    最常见的post提交数据方式
    
2.multipart/form-data
    上传文件
3.application/json
    告诉服务端消息主体是序列化后的json字符串

'''