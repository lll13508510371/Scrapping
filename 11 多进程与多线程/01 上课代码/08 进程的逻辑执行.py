import time
import threading  # 线程模块, 内置模块
import multiprocessing  # 进程模块, 内置模块


def sing():
    """只有函数对象才可以使用多任务(多进程,多线程)"""
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  # 模拟程序阻塞


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)
    # 多进程无法计算时间消耗,
    # print('程序执行花费时间:', time.time() - start_time)

if __name__ == '__main__':
    # 多任务, 对于多进程来说, 必须写在 if __name__ == '__main__': 下面
    # 因为不写在这会找不到主进程

    # start_time = time.time()
    # 将函数对象, 转换成进程程对象, 执行
    multiprocessing.Process(target=sing).start()
    multiprocessing.Process(target=dance).start()



"""
线程的实现步骤
    1. 将函数对象, 转换成线程对象
    2. 执行线程对象任务
    
多进程传参方式和多线程一样
"""