# HTTP 、 TCP 、 socket 之间的关系

'''
Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。
Socket是应用程序通过网络协议进行通信的接口，是应用程序与网络协议根进行交互的接口
使得自己的应用与TCP协议打交道
'''
# socket共有两个端

# ------socket_server 端
import re

'''
一开始的 server 是监听的 server 
后面新生成的 sock,addr 是用来连接客户端的 sock 
所以后面data 需要用sock去连接
'''
# import socket
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 服务器到服务器之间的连接
# server.bind(('0.0.0.0',8000)) # 要传进元组 如果这里是127.0.0.1在本地客户端上就无法连接
# server.listen()
# sock,addr = server.accept()  # 可以点进去查看return
#
# # 获取从客户端发送的数据
# # 一次获取1k的数据
# data = sock.recv(1024)
# print(data.decode("utf-8"))
# sock.send("hello {}".format(data).encode("utf-8"))
# server.close()
# sock.close()


# -------socket_client 端
'''
bind(协议、地址、端口) 端口是为了指明软件
'''
# import socket
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(('127.0.0.1',8000)) # 要传进元组
# client.send("bobby".encode("utf-8"))
# data = client.recv(1024)
# print(data.decode("utf-8")
# client.close()

# ------- 实现一个聊天与多用户连接 -------
# --- server
# import socket
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 服务器到服务器之间的连接
# server.bind(('0.0.0.0',8000)) # 要传进元组 如果这里是127.0.0.1在本地客户端上就无法连接
# server.listen()
# sock,addr = server.accept()  # 可以点进去查看return
# # 持续通信不能close 要一直循环
# while True:
#     data = sock.recv(1024)
#     print(data.decode("utf-8"))
#     re_data = input()
#     sock.send(re_data.encode("utf-8"))

# ---client
# import socket
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(('127.0.0.1',8000)) # 要传进元组
# while True:
#     re_data = input()
#     client.send(re_data.encode("utf-8"))
#     data = client.recv(1024)
#     print(data.decode("utf-8"))

# ---- socket 模拟 http 请求
'''
requests -> urllib -> socket (socket是最底层的, 是操作系统提供给我们的)
与 web相关的连接 (数据库连接，进程之间的通信，网络之间的请求)都是用socket来连接
'''
import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过 socket 请求 html
    url = urlparse(url)
    host = url.netloc # 提取主域名 baiud.com
    path = url.path # 提取子域名 /dos/asd
    if path =="":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,80)) # 要传进元组

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf-8"))

    data = b""
    while True:

        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8")
    # html_data = data.split("\r\n\r\n")[1] # 去掉头信息
    # print(html_data)

    print(data)
    client.close()


if __name__ == '__main__':
    get_url('https://www.baidu.com')

# 最新 socket编程




