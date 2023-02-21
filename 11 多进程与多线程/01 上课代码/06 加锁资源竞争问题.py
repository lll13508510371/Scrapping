import threading
import time
import random


# 创建一把锁
lock = threading.Lock()

def add1(n):
    for i in range(100):
        time.sleep(random.randint(1,3))

        lock.acquire()  # 上锁
        with open('hello.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{n} hello world !' + 'hello world !'*1024)
            f.write('\n')
        lock.release()  # 解锁: 上锁以后要记得解锁, 不然会出现死锁引发报错


if __name__ == '__main__':
    for n in range(10):
        t1 = threading.Thread(target=add1, args=(n, ))
        t1.start()

"""
多线程执行, 如果操作的是敏感资源, 那么会不断的枪这个资源的执行权限, 可能会导致数据产生偏差
    
    针对一个全局变量用多任务操作
    对单个文件用多任务操作

解决方案: 加锁 解锁, 让这个资源有且仅有一个人能操作
"""