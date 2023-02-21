import time


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)  
        ''' 模拟程序阻塞  或者说  模拟网络延迟（比如请求网页等待的时间）'''


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)


start_time = time.time()  # 记录程序开始执行的时间
sing()
dance()
print('程序执行花费时间:', time.time() - start_time)  # 记录整个程序消耗的时间

"""
默认情况下, 程序是单线程
"""