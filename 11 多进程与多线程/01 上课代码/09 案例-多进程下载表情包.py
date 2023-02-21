import multiprocessing
import re
import threading

import requests
import time

def send_request(url):
    """根据地址发送请求的函数"""
    response = requests.get(url=url)
    return response  # 返回响应体对象

def parse_data(data):  # 返回的是列表, 里面是表情包的地址
    """根据传入的数据做解析"""
    result = re.findall(
        '<img class="waitpic" src="https://www.biaoqingbao.net/wp-content/uploads/2020/07/thumb.png" data-original="(.*?)" alt=".*?" >',
        data,
        re.S)

    return result

def save_data(file_name, data):
    """
    保存数据的方法
    :param file_name: 文件名
    :param data: 图片数据
    """
    with open('img\\' + file_name, mode='wb') as f:
        f.write(data)
        print('保存完成:', file_name)

def main(url):
    """主函数: 调度其他三个函数的执行"""
    # 1.调用发送请求的函数
    html_data = send_request(url).text
    # 2.调用数据解析的方法
    imgUrl_list = parse_data(html_data)  # 图片地址列表

    for imgUrl in imgUrl_list:
        file = imgUrl.split('/')[-1]  # 图片文件名
        img_data = send_request(imgUrl).content  # 请求的图片数据

        # 3.调用保存数据的方法
        save_data(file, img_data)

    # 多线程中时间记录需要放到函数中记录
    # print('程序执行花费时间:', time.time() - start_time)


# main('https://www.biaoqingbao.net/gaoxiao/')


# start_time = time.time()  # 记录程序开始执行的时间

if __name__ == '__main__':

    for page in range(1, 6):
        url = f'https://www.biaoqingbao.net/gaoxiao/page_{page}.html'

        # 转化线程对象, 执行线程任务
        multiprocessing.Process(target=main, args=(url,)).start()





