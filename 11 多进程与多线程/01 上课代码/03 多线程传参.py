import threading
import time


def get(url, headers=None):
    print(url)
    time.sleep(5)
    print(headers)


urls = ['https://www.百度.com', 'https://www.豆瓣.com', 'https://www.搜狗.com']

for url in urls:
    threading.Thread(
        target=get,  # 指定需要转化的函数名
        args=(url,),  # 指定位置参数, 只有一个元组的参数需要加逗号
        kwargs={'headers': {'user-agent': 'python'}}  # 指定函数关键字参数
    ).start()
