import multiprocessing
import re
import threading
import concurrent.futures
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


def save_one_pic(img_url):
    """定义一个保存一张图片的函数"""
    img_data = send_request(img_url).content  # # 请求一张图片数据
    file = img_url.split('/')[-1]  # 图片文件名
    save_data(file, img_data)


def main(url):
    """主函数: 调度其他三个函数的执行"""
    # 1.调用发送请求的函数
    html_data = send_request(url).text
    # 2.调用数据解析的方法
    imgUrl_list = parse_data(html_data)  # 图片地址列表

    # 一页有32张图片, 一页的所有图片保存用多线程执行
    """将一张图片的保存逻辑通过多线程分发任务"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for imgUrl in imgUrl_list:
            executor.submit(save_one_pic, imgUrl)


if __name__ == '__main__':

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executer:
        for page in range(1, 6):
            url = f'https://www.biaoqingbao.net/gaoxiao/page_{page}.html'

            # 转化线程对象, 执行线程任务
            # multiprocessing.Process(target=main, args=(url,)).start()

            executer.submit(main, url)

    print('程序执行花费时间:', time.time() - start_time)

# 可以记录池子的运行时间

# 线程是依附于进程运行的
# 把每一个进程下用线程进行任务分发
