"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用多线程采集170页所有数据保存为csv, 计算程序运行的时间
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点  比如香港有热门景点[ 香港海洋公园 、 星光大道 、 维多利亚港 、 太平山 、 尖沙咀 、 金紫荆广场 、 香港迪士尼乐园 、 中环 、 弥敦道 、 兰桂坊 、 中银大厦 、 香港杜莎夫人蜡像馆 、 中环至半山自动扶]
            img_url  # 城市图片url
            
请在下方编写代码：
"""
import csv
import time

import parsel
import requests
import concurrent.futures
#
# url = 'https://place.qyer.com/china/citylist-0-0-1/'
#
# # 2. 发送请求
# response = requests.get(url=url)
# html_data = response.text
# print(html_data)  # 打印确认数据已经是请求到了
#
# # 3. 解析数据
# selector = parsel.Selector(html_data)
# lis = selector.xpath('//ul[@class="plcCitylist"]/li')
#
#
# for li in lis:
#     city_name = li.xpath('.//h3/a/text()').get().strip()
#     travel_people = li.xpath('.//p[@class="beento"]/text()').get().strip()
#     travel_hot = li.xpath('.//p[@class="pois"]/a/text()').getall()
#     travel_hot = [i.strip() for i in  travel_hot]
#     travel_hot = '-'.join(travel_hot)
#
#     img_url = li.xpath('.//p[@class="pics"]//img/@src').get()
#     print(img_url)

import threading

lock = threading.Lock()

# 数据请求
def send_request(url):
    response = requests.get(url=url)
    return response.text

# 数据解析
def parse_data(data):
    selector = parsel.Selector(data)
    lis = selector.xpath('//ul[@class="plcCitylist"]/li')

    # data_list = [] # 收集解析到的每一条数据, 后续return返回
    for li in lis:
        city_name = li.xpath('.//h3/a/text()').get().strip()
        travel_people = li.xpath('.//p[@class="beento"]/text()').get().strip()
        travel_hot = li.xpath('.//p[@class="pois"]/a/text()').getall()
        travel_hot = [i.strip() for i in travel_hot]
        travel_hot = '-'.join(travel_hot)

        img_url = li.xpath('.//p[@class="pics"]//img/@src').get()
        print(city_name, travel_people, travel_hot, img_url)

        # 返回一个生成器对象, 直接遍历得到数据
        yield city_name, travel_people, travel_hot, img_url

# 数据保存
def save_data(data_generator):
    for data in data_generator:
        # print('遍历的每一条数据:', data)

        lock.acquire()
        with open("穷游网.csv", mode='a', newline='', encoding='utf-8') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(data)
        lock.release()

def main(url):
    html_data = send_request(url)
    parse_result = parse_data(html_data)  # 得到一个生成器对象
    save_data(parse_result)


if __name__ == '__main__':
    # 测试主函数运行是否有误
    # main('https://place.qyer.com/china/citylist-0-0-1/')
    # threading   concurrent

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for page in range(1, 171):
            url = f'https://place.qyer.com/china/citylist-0-0-{page}/'
            executor.submit(main, url)

    print('消耗时间:', time.time() - start_time)