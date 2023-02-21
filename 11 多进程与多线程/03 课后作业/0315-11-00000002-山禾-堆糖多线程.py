"""
	目标网址：https://www.duitang.com/

	作业描述：请在网页最上面搜索框输入关键字 “蜡笔小新” 进行搜索图片，根据搜索到的结果采集前十页图片

	作业要求：用多进程嵌套多线程的方式实现
"""
import os
import threading
# import concurrent.futures
import concurrent.futures
import time

import requests


def send_requeset(query_param):
    headers = {
        'referer': 'https://www.duitang.com/search/?kw=蜡笔小新&type=feed',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    url = 'https://www.duitang.com/napi/blogv2/list/by_search/'

    # headers也不能乱加 --> UnicodeEncodeError: 'latin-1' codec can't encode characters in position 35-38: ordinal not in range(256) 这里加headers就是这样
    response = requests.get(url=url, params=query_param)

    return response


def parse_data(response):
    total_data = response.json()

    obj_list = total_data['data']['object_list']

    return obj_list


def save_img(img_url):
    # lock = threading.Lock()
    try:
        img_content = requests.get(img_url, timeout=5).content
        img_name = img_url.split('/')[-1]
        # with lock:  -->  不需要上锁，每一个文件的名字都不同，只有操作相同文件的时候需要🔒
        with open(os.path.join('/Users/lujinghan/PycharmProjects/Scrapping/11 多进程与多线程/03 课后作业/img', img_name),
                  mode='wb') as f:
            f.write(img_content)
            print(f'{img_name}下载成功')

    except Exception:
        pass


def main(query_param):
    time.sleep(1)
    response = send_requeset(query_param)

    obj_list = parse_data(response)

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as T_executor:
        for obj in obj_list:
            img_url = obj['photo']['path']
            T_executor.submit(save_img, img_url)


if __name__ == '__main__':
    if not os.path.exists('/Users/lujinghan/PycharmProjects/Scrapping/11 多进程与多线程/03 课后作业/img'):
        os.mkdir('/Users/lujinghan/PycharmProjects/Scrapping/11 多进程与多线程/03 课后作业/img')

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as P_executor:
        for i in range(0, 24 * 50 + 1, 24):
            query_str_param = {
                'kw': '蜡笔小新',
                'after_id': str(i),
                'type': 'feed',
                'include_fields': 'top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id',
                '_type': '',
                '_': str(int(time.time() * 1000))  # 不检查时间戳，网址输入随便输入一个时间戳字符串都能获得值
            }

            '''！！！！之前这里逻辑有问题，把进程池对象写进循环中了，虽然最终得到了，但这样每一次循环都只有一个进程在运行，下一次循环又是新的进程池对象，然后只提交和运行一个进程'''
            # with concurrent.futures.ProcessPoolExecutor(max_workers=5) as P_executor:
            P_executor.submit(main, query_str_param)

    end_time = time.time()
    # 可以记录池子的运行时间
    print('进程池运行了：', end_time - start_time, '秒')
    # query_str_param = {
    #     'kw': '蜡笔小新',
    #     'after_id': '24',
    #     'type': 'feed',
    #     'include_fields': 'top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id',
    #     '_type': '',
    #     '_': str(int(time.time() * 1000))
    # }
    # main(query_str_param)
'''
我设置设置进程数17（2x核心+1) 或15(2x核心-1)（正常的最优进程数，网上说法不一，还有1：1）， 线程80（10x线程 正常的最优线程数）爬到一半卡住了，不知道什么情况，可能是服务器识别到了你的ip同时过多请求给反扒了吧（只是查询参数不一样，请求的url是一样的，也就是同一个服务器里面找内容）
都设置成5做作业当天都能爬到，但今天快爬完的时候卡住了，但比上面的情况爬的多
然后没办法，只能设置try catch 估计有些图片请求不到或者暂时请求不到或者被反扒（只是查询参数不一样，请求的url是一样的，也就是同一个服务器里面找内容） --> img_content = requests.get(img_url, timeout=5).content
'''
