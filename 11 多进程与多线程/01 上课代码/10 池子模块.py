import time
import concurrent.futures  # 导入池子模块


def thread_function(name):
    print("子线程 %s: 启动" % name)
    time.sleep(2)
    print("子线程 %s: 完成" % name)


if __name__ == '__main__':
    # ThreadPoolExecutor 线程池
    # ProcessPoolExecutor 进程池
    # max_workers 指定最大任务数
    # submit 往池子中提交任务
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executer:
        for i in range(10):
            executer.submit(thread_function, i)
