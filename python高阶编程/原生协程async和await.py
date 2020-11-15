''' asyncio
包含各种特定系统实现的模块化事件循环
传输和协议抽象
对TCP,UDP,SSL 子进程 演示调用以及其他的具体支持
模仿futures模块但使用与事件循环
基于yield from 的协议和任务 可以让你用顺序的方式编写并发代码
必须使用一个将产生阻塞IO的调用时，有接口可以把这个事件转移到线程池
模仿threading模块中的同步原语、可以用在单线程内的协程之间
'''
# await 相当于 yield from
# 高并发实现具备的三个要素:事件循环+回调(驱动生成器)+epoll(IO多路复用)
# asyncio python用于解决异步io的一整套方案

# -----运行一个简单的异步io
# import asyncio
# import time
# async def get_html():
#     print("start get url")
#     await asyncio.sleep(2) # 这会返回一个future
#     print("end get url")
# if __name__ == "__main__":
#     # 创建了事件循环将协程注册到循环队列里面,只代表了运行协程(并不存在异步)
#     # 所以需要增加一个future类
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html() for i in range(20)]
#     # loop.run_until_complete(get_html()) # 一个协程注册到loop里面
#     loop.run_until_complete(asyncio.wait(tasks)) # 并发 asyncio.wait(可迭代对象) 一次性提交多个任务 要用到wait
#     print(time.time()-start_time)

# ------- 获取返回值 回调函数
'''
asyncio.ensure_future(get_html())
loop.create_task(get_html())

task.add_done_callback(函数名) 
task.add_done_callback(partial(参数名,函数名))
'''
# import asyncio
# import time
# from functools import partial # 可以将函数包装成另外一个函数
#
# async def get_html():
#     print("start get url")
#     await asyncio.sleep(2) # 这会返回一个future
#     return "bobby"
#
# # def callback(future):  # 会将future(task)传递进来
# #     print("send email to u")
# def callback(url,name,future):  # 如果要用partial传参,参数必须要放在第一位
#     print(url)
#     print(name)
#     print("send email to u")
#
# if __name__ == "__main__":
#
#     loop = asyncio.get_event_loop()
#     # en_fu 与 cr_ta 两个方法等效
#     # get_future = asyncio.ensure_future(get_html()) # 获得一个future对象
#     # loop.run_until_complete(get_future) # 可接受future 协程 task 类型
#     # print(get_future.result())
#     task = loop.create_task(get_html())  # 返回的是task类型 (task是future的一个子类)
#     #task.add_done_callback(callback)  # 只接受参数名 不能接受其他参数,我们可以用 partial 解决这个问题
#     task.add_done_callback(partial(callback,"www.baidu.com","baidu"))
#     loop.run_until_complete(task)
#     print(task.result())


# ---------- wait 和 gather 区别
'''
gather 可以将 tasks 分组
'''
# import asyncio
# import time
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
# if __name__ == "__main__":
#
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("asduio") for i in range(20)]
#     # # loop.run_until_complete(asyncio.wait(tasks))
#     # loop.run_until_complete(asyncio.gather(*tasks)) # 要在前面加个*
#
#     group1 = [get_html("baidu")for i in range(2)]
#     group2 = [get_html("sdf")for i in range(2)]
#     # group1 = asyncio.gather(*group1)
#     # group1.cancel() # 可以将整个组取消掉
#     loop.run_until_complete(asyncio.gather(*group1,*group2))

# ------- run_until_complete

# loop.run_forever() # 会一直运行不会停止

# 1. loop会被放到future中

# 2. 取消future(task) 在cmd中运行 然后按ctrl+c 强制取消

# import asyncio,time
# async def get_html(sleep_times):
#     print("waiting")
#     await asyncio.sleep(sleep_times)
#     print("done after {}s".format(sleep_times))
# if __name__ == "__main__":
#     task1 = get_html(1)
#     task2 = get_html(2)
#     task3 = get_html(3)
#     tasks = [task1,task2,task3]
#
#     loop = asyncio.get_event_loop()
#     # 想需要loop 需要try
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e:
#         all_tasks = asyncio.Task.all_tasks()
#         for task in all_tasks:
#             print("cancel task")
#             print(task.cancel())
#         loop.stop()
#         loop.run_forever() # stop完后一定要run_forever()
#     finally:
#         loop.close()

# ---------call_soon , call_later , call_at call_soon_threadsafe
'''
希望在循环体系中插入定制的函数
一些很底层的方法，基本不会用到
'''
# import asyncio
#
# def callback(sleep_times):
#     print("sleep {} success:".format(sleep_times))
# def stoploop(loop):
#     loop.stop()
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
    # -- call_soon

    # loop.call_soon(callback,2) # 在队列中直接运行

    # --call_soon  call_later

    # loop.call_later(2,callback,2) # 根据延迟时间定义顺序 第一参数延迟time 第二个func 第三个参数
    # loop.call_later(1,callback,1)
    # loop.call_soon(callback,4)  # 优先度高于call_later

    # --- call_at 在当前时间运行
    # now = loop.time()
    # loop.call_at(now+1,callback,1)
    # loop.call_at(now+2,callback,2)
    # loop.call_soon(callback,4)
    # loop.run_forever() # 与loop.run_until_complete()都是注册任务到loop里


    # --- call_soon_threadsafe 与 call_soon方法一样

# ------- asyncio 对接多线程
'''
多线程: 在协程中集成阻塞io
'''
# import asyncio
# from concurrent.futures import ThreadPoolExecutor
# import socket
# from urllib.parse import urlparse
#
#
# def get_url(url):
#     #通过socket请求html
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
#     if path == "":
#         path = "/"
#
#     #建立socket连接
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # client.setblocking(False)
#     client.connect((host, 80)) #阻塞不会消耗cpu
#
#     #不停的询问连接是否建立好， 需要while循环不停的去检查状态
#     #做计算任务或者再次发起其他的连接请求
#
#     client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
#
#     data = b""
#     while True:
#         d = client.recv(1024)
#         if d:
#             data += d
#         else:
#             break
#
#     data = data.decode("utf8")
#     html_data = data.split("\r\n\r\n")[1]
#     print(html_data)
#     client.close()
#
#
# if __name__ == "__main__":
#     import time
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     executor = ThreadPoolExecutor(3)
#     tasks = []
#     for url in range(20):
#         url = "http://shop.projectsedu.com/goods/{}/".format(url)
#         task = loop.run_in_executor(executor, get_url, url) # 将某个阻塞io 放到线程池里面运行
#         tasks.append(task)
#     loop.run_until_complete(asyncio.wait(tasks))
#     print("last time:{}".format(time.time()-start_time))

# ----------asyncio 模拟http请求
# asyncio 没有提供http协议的接口
# import asyncio
# import socket
# from urllib.parse import urlparse
#
#
# async def get_url(url):
#     #通过socket请求html
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
#     if path == "":
#         path = "/"
#
#     #建立socket连接
#     reader, writer = await asyncio.open_connection(host,80)
#     writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
#     all_lines = []
#     async for raw_line in reader:
#         data = raw_line.decode("utf8")
#         all_lines.append(data)
#     html = "\n".join(all_lines)
#     return html
#
# async def main():
#     tasks = []
#     for url in range(20):
#         url = "http://shop.projectsedu.com/goods/{}/".format(url)
#         tasks.append(asyncio.ensure_future(get_url(url)))
#     for task in asyncio.as_completed(tasks):
#         result = await task
#         print(result)
#
# if __name__ == "__main__":
#     import time
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     print('last time:{}'.format(time.time()-start_time))











