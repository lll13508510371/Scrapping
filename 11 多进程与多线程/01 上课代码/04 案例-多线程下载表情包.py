import re
import threading

import requests
import time
#
#
# start_time = time.time()  # 记录程序开始执行的时间
#
# def haha():
#     for page in range(1, 6):
#         print(f'====================正在抓取第{page}页数据================')
#         response = requests.get(f'https://www.biaoqingbao.net/gaoxiao/page_{page}.html')
#         html_data = response.text
#         print(html_data)
#
#         # 解析数据
#         """
#         <img class="waitpic" src="https://www.biaoqingbao.net/wp-content/uploads/2020/07/thumb.png" data-original="https://www.biaoqingbao.net/wp-content/uploads/2022/07/006BkP2Hly1h4fpmyuo9yg30500507wh-150x150.gif" alt="二次元跳舞表情包" >
#         <img class="waitpic" src="https://www.biaoqingbao.net/wp-content/uploads/2020/07/thumb.png" data-original="(.*?)" alt=".*?" >
#         """
#         result = re.findall('<img class="waitpic" src="https://www.biaoqingbao.net/wp-content/uploads/2020/07/thumb.png" data-original="(.*?)" alt=".*?" >',
#                    html_data,
#                    re.S)
#
#         print(result)
#         print(len(result))
#
#         for img_url in result:
#             try:
#                 # 请求图片数据
#                 img_data = requests.get(img_url).content
#
#                 # 准备一个文件名
#                 file_name = img_url.split('/')[-1]
#
#                 with open('img\\' + file_name, mode='wb') as f:
#                     f.write(img_data)
#                     print('保存完成:', file_name)
#             except Exception as e:
#                 pass
#
# print('程序执行花费时间:', time.time() - start_time)

# 函数: 一个函数只做一件事情
#       请求
#       解析
#       保存

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
    print('程序执行花费时间:', time.time() - start_time)


# 当主函数写完后, 一定要测试主函数运行有没有问题
# 因为在多任务中, 一旦程序报错, 可能不会中断, 而且错误很难排查
# main('https://www.biaoqingbao.net/gaoxiao/')


start_time = time.time()  # 记录程序开始执行的时间

for page in range(1, 6):
    url = f'https://www.biaoqingbao.net/gaoxiao/page_{page}.html'

    # 转化线程对象, 执行线程任务
    threading.Thread(target=main, args=(url,)).start()


"""
目前有多少个线程任务?
    主线程 + 5个子线程 = 6个
    
线程任务数不是越多越好?
因为线程最终是压榨了计算机的性能

通过多线程提升了代码效率大概是5  6 倍

scrapy  底层是基于异步实现


"""




