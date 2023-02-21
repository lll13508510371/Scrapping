"""
	目标网址：https://www.duitang.com/

	作业描述：请在网页最上面搜索框输入关键字 “蜡笔小新” 进行搜索图片，根据搜索到的结果采集前十页图片

	作业要求：用多进程嵌套多线程的方式实现
"""
import concurrent.futures
import threading
import time
import requests

lock = threading.Lock()

# 数据请求
def send_request(url):
    response = requests.get(url=url)
    return response

# 数据解析
def parse_data(data):
    data_list = data['data']['object_list']

    img_url_list = []
    for data in data_list:
        img_url = data['photo']['path']
        img_url_list.append(img_url)

    return img_url_list

# 每一页的请求用进程, 每一页的每张图片用线程保存
# 定义一个保存一张图片的函数, 这个函数用多线程去跑
def save_ong_img(img_url):
    img_data = send_request(img_url).content  # 请求每一张图片
    file_name = img_url.split('/')[-1]
    with open('img\\' + file_name, mode='wb') as f:
        f.write(img_data)
        print('保存完成:', file_name)

def main(url):
    json_data = send_request(url).json()
    # print(json_data)
    imgUrl_list = parse_data(json_data)  # 得到图片地址列表
    # print(imgUrl_list)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for imgUrl in imgUrl_list:
            executor.submit(save_ong_img, imgUrl)

if __name__ == '__main__':
    # main('https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%98%9F&after_id=48&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1676289161640')
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        for page in range(10):
            url = f'https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%98%9F&after_id={page * 24}&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1676289161640'
            executor.submit(main, url)
    print('消耗时间:', time.time() - start_time)

    # 一般多进程 电脑核数 * 2 + 1
