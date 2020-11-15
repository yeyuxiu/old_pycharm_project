# 数据写入 输出操作时需要用到锁
# 锁的存在是为了线程之间互不干扰又互相运行(11-4视频08:00)
'''
1. 用锁会影响性能
2. 锁会引起死锁
'''
'''
GIL(全局解释锁)/Lock(指令锁)/RLock(可重入锁)
Semaphore(共享对象访问)
Event(线程间通信)
Condition(线程同步)

Lock & RLock : 互斥锁 用来保证多线程访问共享变量的问题
Semaphore对象 ： Lock互斥锁的加强版，可以被多个线程同时拥有，而Lock只能被某一个线程同时拥有。
Event对象 : 它是线程间通信的方式，相当于信号，一个线程可以给另外一个线程发送信号后让其执行操作。
Condition对象 ：其可以在某些事件触发或者达到特定的条件后才处理数据
'''

# ----GIL-----
# python 中一个线程对应于c语言中的一个线程
# GIL使得提供一时刻只有一个线程运行在一个CPU上执行字节码,无法将多个线程映射到多个CPU上
# GIL会根据执行的字节码行数以及时间片释放GIL,GIL在遇到io操作的时候主动释放
# CPython 中还有另一个机制，叫做间隔式检查（check_interval），意思是 CPython 解释器会去轮询检查线程 GIL 的锁住情况，每隔一段时间，Python 解释器就会强制当前线程去释放 GIL，这样别的线程才能有执行的机会。
# Python的多线程在多核CPU上，只对于IO密集型计算产生正面效果；而当有至少有一个CPU密集型线程存在，那么多线程效率会由于GIL而大幅下降。
# 如果是计算密集型的 利用多进程可以好好解决多线程GIL的短处
# 因为GIL的存在，只有IO Bound场景下得多线程会得到较好的性能
# 如果对并行计算性能较高的程序可以考虑把核心部分也成C模块，或者索性用其他语言实现
# GIL在较长一段时间内将会继续存在，但是会不断对其进行改进
'''
CPython 使用引用计数来管理内容，所有 Python 脚本中创建的实例，都会配备一个引用计数，来记录有多少个指针来指向它。
当实例的引用计数的值为 0 时，会自动释放其所占的内存。
假设有两个 Python 线程同时引用 a，那么双方就都会尝试操作该数据，很有可能造成引用计数的条件竞争，
导致引用计数只增加 1（实际应增加 2），这造成的后果是，当第一个线程结束时，会把引用计数减少 1，
此时可能已经达到释放内存的条件（引用计数为 0），当第 2 个线程再次视图访问 a 时，就无法找到有效的内存了。
所以，CPython 引进 GIL，可以最大程度上规避类似内存管理这样复杂的竞争风险问题。
'''
# import sys
# a = []
# b = a
# print(sys.getrefcount(a)) #查看引用计数

# ---- 展示了其实GIL也不一定是锁死一个程序
# total = 0
# def add():
#     # 1.dosometing1
#     # 2.io操作
#     # 3.dosometing
#     global total
#     for i in range(1000000):
#         total += 1
# def desc():
#     global total
#     for i in range(1000000):
#         total -= 1
# import threading
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(total)

# ------Lock(互斥锁)(一把钥匙所有线程竞争)--------
# threading.Lock
# 请求锁定 — 进入锁定池等待 — 获取锁 — 已锁定 — 释放锁
'''
acquire([timeout]): 使线程进入同步阻塞状态，尝试获得锁定。
release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。
'''
# from threading import Lock
# import threading
# total = 0
# lock = Lock()
# def add():
#     # 1.dosometing1
#     # 2.io操作
#     # 3.dosometing
#     global total
#     global lock
#     for i in range(1000000):
#         lock.acquire()
#         total += 1
#         lock.release()
# def desc():
#     global total
#     global lock
#     for i in range(1000000):
#         lock.acquire()
#         total -= 1
#         lock.release()
#
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(total)



# --------Rlock(可重入锁)------
# 在同一个线程里面，可以连续调用多次Rlock.acquire() (注意acquire和releadse次数要相等)
# threading.Rlock
'''
可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。
'''


# --------Semaphore(信号量)-------
'''
Semaphore管理一个内置的计数器，
每当调用acquire()时内置计数器-1；
调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
'''
# import time
# import threading
# semaphore = threading.Semaphore(3) # 内置计数器为3 允许3个线程访问
# def func():
#     if semaphore.acquire():
#         for i in range(3):
#             time.sleep(1)
#             print(threading.currentThread().getName()+'获得锁')
#         semaphore.release()
#         print(threading.currentThread().getName()+'释放锁')
#
# for i in range(5):
#     t1 = threading.Thread(target=func)
#     t1.start()


# ------Event(线程间通信)------
'''
Event内部包含了一个标志位，初始的时候为false。
可以使用使用set()来将其设置为true；
或者使用clear()将其从新设置为false；
可以使用is_set()来检查标志位的状态；
wait(timeout=None)阻塞当前线程直到event的内部标志位被设置为true或者timeout超时。
'''
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def __init__(self, signal):
#         threading.Thread.__init__(self)
#         self.singal = signal
#
#     def run(self):
#         print ("I am %s,I will sleep ..."%self.name)
#         self.singal.wait()
#         print ("I am %s, I awake..." %self.name)
#
# if __name__ == "__main__":
#     singal = threading.Event()
#     for t in range(0, 3):
#         thread = MyThread(singal)
#         thread.start()
#     print ("main thread sleep 3 seconds... ")
#     time.sleep(3)
#     singal.set()

# -------Condition(条件变量)
# 用于复杂的线程间同步
'''
acquire(): 线程锁
release(): 释放锁
wait(timeout): (进入condition等待池等待,释放锁)线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。
notify(n=1): (从等待池中挑选一个线程并通知,通知后运行)通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。
notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程
'''
# import threading
# import time
# con = threading.Condition()
#
# num = 0
# # 生产者
# class Producer(threading.Thread):
#
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         # 锁定线程
#         global num
#         con.acquire()
#         while True:
#             print ("开始添加！！！")
#             num += 1
#             print ("火锅里面鱼丸个数：%s" % str(num))
#             time.sleep(1)
#             if num >= 5:
#                 print ("火锅里面里面鱼丸数量已经到达5个，无法添加了！")
#                 # 唤醒等待的线程
#                 con.notify()  # 唤醒小伙伴开吃啦
#                 # 等待通知
#                 con.wait()
#         # 释放锁
#         con.release()
#
# # 消费者
# class Consumers(threading.Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         con.acquire()
#         global num
#         while True:
#             print ("开始吃啦！！！")
#             num -= 1
#             print ("火锅里面剩余鱼丸数量：%s" %str(num))
#             time.sleep(2)
#             if num <= 0:
#                 print ("锅底没货了，赶紧加鱼丸吧！")
#                 con.notify()  # 唤醒其它线程
#                 # 等待通知
#                 con.wait()
#         con.release()
#
# p = Producer('p')
# c = Consumers('c')
# p.start()
# c.start()
