import time
import threading  # 线程模块, 内置模块


def sing():
    """只有函数对象才可以使用多任务(多进程,多线程)"""
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  # 模拟程序阻塞


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)
        # 如果要计算线程执行时间, 只能写到线程对应的函数里面计算时间
    print('程序执行花费时间:', time.time() - start_time)


start_time = time.time()  # 记录程序开始执行的时间
print('当前的线程数量:', threading.enumerate())  # threading.enumerate() 查看当前线程数量的方法

# 1. 将函数对象, 转换成线程对象
sing_thread = threading.Thread(target=sing).start()  # 支持链式调用
# sing_thread.start()

print('当前的线程数量:', threading.enumerate())

# 2. 执行线程对象任务 <线程对象.start()>
dance_thread = threading.Thread(target=dance)
dance_thread.start()

print('当前的线程数量:', threading.enumerate())



"""
线程的实现步骤
    1. 将函数对象, 转换成线程对象
    2. 执行线程对象任务
"""