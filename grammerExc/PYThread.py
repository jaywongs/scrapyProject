# -*-coding:utf-8-*-

import threading
import time

# #为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0;
#     while count < 5:
#         time.sleep(delay)
#         count += 1;
#         print "%s: %s" % ( thread, time.ctime(time.time()))
#
# #创建连个线程
# try:
#     thread.start_new_thread(print_time, ("Thread-1",2,))
#     thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print "Error: unable to start thread"
#
# while 1:
#     pass

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        threadLock.acquire()  # 加锁
        print "Starting:" + self.name
        print_time(self.name, self.counter, 5)
        threadLock.release() #释放锁
        print  "Exiting:" + self.name

threadLock = threading.Lock()
threads = []

# 打印线程函数
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

#创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)

thread1.start()
thread2.start()
thread3.start()

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

for t in threads:
    t.join()
print "exiting main thread"