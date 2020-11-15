# python标准库四种队列 : queue.Queue/asyncio.Queue/multiprocessing.Queue/collections.deque

# Queue模块提供了同步的、线程安全的队列类

# 1.FIFO (先进先出)
# 2.LIFO (后进先出)
# 3.Priority (优先级队列)，优先级队列中的任务顺序跟放入时的顺序是无关的，而是按照任务的大小来排序，最小值先被取出
# 如果是列表或者元祖，则先比较第一个元素，然后比较第二个，以此类推，直到比较出结果

# queue_FIFO = queue.Queue(maxsize=10000) # FIFO队列 设置放入的元素种数，maxsize <= 0则队列无限大
# queue_LIFO = queue.LifoQueue(maxsize = 10000) # LIFO队列
# queue_PRI = queue.PriorityQueue(maxsize= 10000)# Priority队列

'''
exception (对象名).empty() # 对象为空时调用非阻塞get() / get_nowait()时引发异常
exception (对象名).full() # 对象已满调用非阻塞 put() / put_nowait() 时引发异常

对象名.qsize() # 返回队列大小 
empty() # 如果队列为空则返回True
full() # 如果队列已满则返回True
put(item[,block[,timeout]]) # 添加任务
# queue.put(item,True,2) 将item插入队列中，如果队列阻塞则阻塞2秒，2秒后引发full异常
# 如果timeout 时整数，他会阻止最大超时时间，如果在该时间内没有可用的空闲槽，则会引发Full异常。
# 反之（block为false），如果有空闲槽可以立即使用，则将item放入队列，否则引发Full异常（在这种情况下忽略超时）。
put_nowait(item) # = put(item,False)


get([block[,timeout]]) # 获取并删除一个项目，当队列空时调用该函数会一直阻塞，直到队列中有任务可获取为止。如果 timeout 是正数，则最多阻塞 timeout 秒，如果这段时间内还没有任务可获取，则会引发Empty 异常。
get_nowait() # = get(False) 如果有item可以立即使用，则返回该tem，否则引发Empty异常（在这种情况下忽略超时）。
---- 支持跟踪守护进程、消费者线程食肉已完全处理入队任务:
task_done() # 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号。每个get()调用得到一个任务，接下来task_done()调用告诉队列该任务已经处理完毕。
join() # 实际上意味着等到队列为空，再执行别的操作
只要有数据被加入队列，未完成的任务数就会增加。当消费者线程调用task_done()（意味着有消费者取得任务并完成任务），未完成的任务数就会减少。当未完成的任务数降到0，join()解除阻塞。
# 每task_done一次 就从队列里删掉一个元素，这样在最后join的时候根据队列长度是否为零来判断队列是否结束，从而执行主线程。
# 放入队列的个数要和 task_done 调用次数相等，也就是说你每取出来一个，必须 task_done ，要不然计数不相等， join 的时候就不知道什么时候退出
'''
# import queue
# q = queue.Queue(maxsize=1) # 100为1个项目存入queue中而不是100个
# q.put(100)
# # q.put_nowait(100)
# print(q.get())
# print(q.empty())
# q.put(2)
# print(q.qsize())

import threading
from queue import Queue
from time import sleep
# self.queue.task_done() 去掉可以正常运行
que = Queue()
class Testthread(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.queue = que
    def run(self):
        while True:
            sleep(0.1)
            item = self.queue.get()
            print(item)
            #self.queue.task_done()
tasks = [Testthread(que) for x in range(2)]
for x in tasks:
    t = Testthread(que)
    t.setDaemon(True)
    t.start()
for x in range(10):
    que.put(x)
que.join()

# ------- deque(双向队列) 与 时间复杂度O(1)
'''
appendleft() # 添加一个元素 左
extendleft() # 添加一组元素 左
popleft() # 弹出一个元素 
insert(index,x) # 插入到指定位置 
rotate(n) # 从尾部旋转到首部(n个元素) 顺时针
rotate(-n) # 从首部旋转到尾部 逆时针
append()
extend() # 一组
pop()  
count() # 计算队列元素数 
clear() # 清除队列
index(x,start,end) # 要查找的元素
remoce(x) # 删除指定元素
reverse() # 队列翻转 
'''
# from collections import deque
# q = deque()
# list1 = [1,2,3,4,5]
# q.extendleft(list1) # [5, 4, 3, 2, 1]
# q.rotate(2) # [2, 1, 5, 4, 3]
# test_index = q.index(2,0,4) # ValueError: '2' is not in deque # 找到则返回位置
'''
题目
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
'''
# from collections import deque
# class MyDeque(object):
#     def __init__(self,*args):
#         self.q = deque()
#         self.q.extend(args)
#     def max_value(self) -> int:
#         return max(self.q) if self.q else -1
#     def push_back(self,x):
#         return self.q.append(x)
#     def pop_front(self):
#         return self.q.popleft() if self.q else -1

