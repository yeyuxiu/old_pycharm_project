'''
thread 的使用(方法、类)

mulProcess 使用

线程池(concurrent future)

'''
# -----多线程(treading)编程 -----
'''
对于io操作来说，多线程和多进程性能差别不大
'''
# ****1. 通过Thread类实例化(适合代码量少)
# import time
# def get_detail_html(url):
#     print("get detail html started 1")
#     time.sleep(2)
#     print("get detail html end 1")
# def get_detail_url(url):
#     print("get detail url started 2")
#     time.sleep(3)
#     print("get detail url end 2")
#
# if __name__ == '__main__':
#     import threading
#     thread1 = threading.Thread(target=get_detail_html,args=("",))  # target = 我们线程要执行的函数(传递函数名) args = 传递(函数)参数
#     thread2 = threading.Thread(target=get_detail_url, args=("",))
#     # 当主线程退出的时候，子线程会停止(t1,t2,main线程同时运行，main运行完后退出程序，所以没有了get detail url end)
#     # 因为并发运行，所以当 t2 的时间 < t1 的时间,会先运行完 t2线程
#     # thread1.setDaemon(True) # 守护线程 (主线程退出，子线程退出)
#     # thread2.setDaemon(True)
#     start_time = time.time()
#     thread1.start() # 启动线程
#     thread2.start()
#
#     thread1.join() # 造成阻塞 等待这两个线程执行完，才会执行主线程
#     thread2.join()
#
#     # 返回0.0 的原因是 这里有3个线程，t1,t2外还有个主线程，都是并行的，所以一开始就运行了t1,t2,time.time()-start_time
#     print("time:{}".format(time.time()-start_time))

# *****2. 通过继承 Thread来实现多线程(适合代码量大)
# import threading,time
# class GetDetailHtml(threading.Thread):
#     def __init__(self,name):
#         super().__init__(name=name)
#     def run(self):
#         print("get detail html started 1")
#         time.sleep(2)
#         print("get detail html end 1")
# class GetDetailUrl(threading.Thread):
#     def __init__(self,name):
#         super().__init__(name=name)
#     def run(self):
#         print("get detail url started 2")
#         time.sleep(3)
#         print("get detail url end 2")
#
# if __name__ == '__main__':
#     thread1 = GetDetailHtml("get_detaile_html")
#     thread2 = GetDetailUrl("get_detaile_url")
#     start_time = time.time()
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()
#     print("time:{}".format(time.time()-start_time))
''' 
构造方法：
Thread(group=None, target=None, name=None, args=(), kwargs={})

　　group: 线程组，目前还没有实现，库引用中提示必须是None；
　　target: 要执行的方法；
　　name: 线程名；
　　args / kwargs: 要传入方法的参数。

实例方法：
　　isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。
　　get / setName(name): 获取 / 设置线程名。

　　start(): 线程准备就绪，等待CPU调度
　　 is / setDaemon(bool): 获取 / 设置是后台线程（默认前台线程（False））。（在start之前设置）

　　　　如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
　　如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
　　start(): 启动线程。
　　join([timeout]):阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
'''
# -------多进程编程(multiprocess)--
# --------子进程有print()的话 idle是无法输出的 要在cmd中才有输出结果
'''
对某些耗cpu的操作，多线程操作就无法达到多核的运用所以有了多进程
对于io操作，运用多线程
对于操作系统来说，切换进程花销要比线程大
尽量使用多线程少用多进程
'''
# 1.消耗cpu操作，计算，挖矿，图表(多进程优于多线程)
# 2.7456576824188232 普通
# 3.013014793395996 多线程(3)
# 2.2739901542663574 多进程(3)
# import time
# from concurrent.futures import ThreadPoolExecutor,as_completed
# from concurrent.futures import ProcessPoolExecutor

# def fib(n):
#     if n<=2:
#         return 1
#     return fib(n-1) + fib(n-2)
# if __name__ == '__main__':
#     with ProcessPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib,(num))for num in range(25,35)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#         print(time.time()-start_time)


# 2.对于io操作来说 多线程优于多进程
# 20.220953464508057 多进程(3)
# 20.007930755615234 多线程(3)
# 2*30s               普通
# def random_sleep(n):
#     time.sleep(n)
#     return n
# if __name__ == '__main__':
#     with ThreadPoolExecutor(3) as executor:
#         all_task = [executor.submit(random_sleep,(n))for n in [2]*30]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#         print(time.time()-start_time)

'''
Process([group [, target [, name [, args [, kwargs]]]]])
1.target：传递一个函数的引用，可以认为这个子进程就是执行这个函数的代码，这里传的是函数的引用，后面不能有小括号
2.args：给target指定的函数传递的参数，以元组的方式传递，这里必须是一个元组，如果不是元组会报TypeError，只有一个参数时要注意别出错
3.kwargs：给target指定的函数传递关键字参数，以字典的方式传递，这里必须是一个字典
4.name：给进程设定一个名字，可以不设定
5.group：指定进程组，大多数情况下用不到

Process的常用方法：
1.start()：启动子进程实例（创建子进程）
2.is_alive()：判断子进程是否还在活着
3.join([timeout])：是否等待子进程执行结束，或等待多少秒
4.terminate()：不管任务是否完成，立即终止子进程

Process的常用属性：
1.name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
2.pid：当前进程的pid（进程号）

获取当前进程的id和当前进程的父进程的id,需要使用os模块：
1.os.getpid()：获取当前进程的id
2.os.getppid() ：获取当前进程的父进程的id
'''
# windows下运行多进程 必须要有__name__ == '__main__' (linux不用)

# import multiprocessing
# import time
# def get_html(n):
#     time.sleep(n)
#     print("sub_process suc")
#     return n
# if __name__ == '__main__':
#     process = multiprocessing.Process(target=get_html,args=(2,))
#     process.start()
#     print(process.pid)
#     process.join()
#     print("main process end")

# -----进程池操作
'''
apply_async(func,args) 从进程池中取出一个进程执行func，args为func的参数。它将返回一个AsyncResult的对象，你可以对该对象调用get()方法以获得结果。
close() 进程池不再创建新的进程
join() wait进程池中的全部进程。必须对Pool先调用close()方法才能join。
'''
# if __name__ == '__main__':
#
#     pool = multiprocessing.Pool(multiprocessing.cpu_count()) # 有多少个cpu就开多少个进程
#     result = pool.apply_async(get_html,args=(3,))
#
#     # 等待所有任务完成
#     pool.close()
#     pool.join()
#     print(result.get())

# 进程共享变量
'''
from queue import Queue # 线程通信使用
from multiprocessing import Queue # 进程通信使用
from multiprocessing import Manger # 进程pool间的通信
manger_queue = Manger().Queue()

'''
import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == "__main__":
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# 共享全局变量通信
# 共享全局变量不能适用于多进程编程，可以适用于多线程

# def producer(a):
#     a += 100
#     time.sleep(2)
#
# def consumer(a):
#     time.sleep(2)
#     print(a)
#
# if __name__ == "__main__":
#     a = 1
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# multiprocessing中的queue不能用于pool进程池
# pool中的进程间通信需要使用manager中的queue

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == "__main__":
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#
#     pool.close()
#     pool.join()

# 通过pipe实现进程间通信
# pipe的性能高于queue

def producer(pipe):
    pipe.send("bobby")

def consumer(pipe):
    print(pipe.recv())

if __name__ == "__main__":
    recevie_pipe, send_pipe = Pipe()
    #pipe只能适用于两个进程
    my_producer= Process(target=producer, args=(send_pipe, ))
    my_consumer = Process(target=consumer, args=(recevie_pipe,))

    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

# def add_data(p_dict, key, value):
#     p_dict[key] = value
#
# if __name__ == "__main__":
#     progress_dict = Manager().dict()
#     from queue import PriorityQueue
#
#     first_progress = Process(target=add_data, args=(progress_dict, "bobby1", 22))
#     second_progress = Process(target=add_data, args=(progress_dict, "bobby2", 23))
#
#     first_progress.start()
#     second_progress.start()
#     first_progress.join()
#     second_progress.join()
#
#     print(progress_dict)


# ------- 进线程池(concurrent.futures.Thread/Process)
# 两个子类操作池
# concurrent.futures.ThreadPoolExecutor(max_workers)   线程池
# concurrent.futures.ProcessPoolExecutor(max_workers)     进程池
# 具有线程池和进程池、管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能。
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程多进程编码，接口一致
'''
concurrent.futures.Executor: 这是一个虚拟基类，提供了异步执行的方法。
submit(function, argument): 调度函数（可调用的对象）的执行，将 argument 作为参数传入函数。
map(func, *iterables, timeout=None): 将 argu ment 作为参数执行函数，以 异步 的方式。
shutdown(Wait=True): 释放所有资源的信号。
concurrent.futures.Future: 其中包括函数的异步执行。Future对象是submit任务（即带有参数的functions）到executor的实例。
'''
# from concurrent.futures import ThreadPoolExecutor,as_completed,wait
# import time
# def get_html(times):
#     time.sleep(times)
#     print("got {} page suc".format(times))
#     return times
#
# executor = ThreadPoolExecutor(max_workers=2)

# # 如果要获取已经成果的task的返回值(as_complete)(按顺序)
# urls = [3,2,4]
# all_task = [executor.submit(get_html,url) for url in urls]
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page".format(data))
#
# # 通过executor的map获取已经完成task(顺序与urls里的一样)
# urls = [3,2,4]
# for data in executor.map(get_html,urls):
#     # 直接yield futures.result() 可以点进map查看
#     print("get {} page".format(data))

# ------wait() 等线程运行完后再运行后面的代码 (取消注释)
# urls = [1,2,3]
# all_task = [executor.submit(get_html,url) for url in urls]
# # wait(all_task)
# print("done")

# *------普通用法 (done(),result(),cancle(),创建线程池)
# from concurrent.futures import ThreadPoolExecutor
# import time
# def get_html(times):
#     time.sleep(times)
#     print("got {} page suc".format(times))
#     return times
# executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池,submit是立即返回(非阻塞)(task1,task2,主线程同功能是运行)
# task1 = executor.submit(get_html,(2))
# task2 = executor.submit(get_html,(3))
# # done方法用于判定某个任务是否完成
# print(task1.done())
# # futures.cancel() 取消任务,任务未执行才能取消 取消成功返回True
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
# # result() 可以获取执行结果
# print(task1.result())


