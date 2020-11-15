# Fiddler
'''
在tools HTTPS中配置 Decrypt HTTPS tracfic 下面是选择监听浏览器还是远程服务
Connetion中配置 端口跟 Allow remove
在CHrome中 配置 SwichProxy 新建监听连接 名字 ip地址 + 端口号 然后重启抓包工具即可
'''
# 使用
# TOOLS里面的TextWizard  可以类似于网上的在线 urlencode base64 的操作
# Rules 大多是隐藏请求 automatic break 自动打断点 还有设置UserAgent
# 在Fiddle最下面命令行中输入 bpu https://www.baidu.com
# bpafter 截取 Response包
# bpa/bpu 就可以取消之前的命令行
# mitproxy
'''
在cmd中 设置 mitmdump -w 文件名 然后选择SwitchProxy

mitmdump -p 端口号 -s py文件
'''

# Packet  Capture
'''
在app上安装运行  https://www.coolapk.com/apk/app.greyshirts.sslcapture
'''