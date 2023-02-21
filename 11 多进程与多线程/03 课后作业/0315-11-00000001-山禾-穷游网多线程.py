"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用多线程采集170页所有数据保存为csv, 计算程序运行的时间
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点  比如香港有热门景点   [香港海洋公园、 星光大道 、 维多利亚港 、 太平山 、 尖沙咀 、 金紫荆广场 、 香港迪士尼乐园 、 中环 、 弥敦道 、 兰桂坊 、 中银大厦、 香港杜莎夫人蜡像馆、 中环至半山自动扶]
            img_url  # 城市图片url

请在下方编写代码：
"""
import csv
import os
import threading
import time
import parsel
import requests


def send_requeset(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    return response


def parse_save_data(html_data):
    # html_data = response.text
    # print(html_data)
    selector = parsel.Selector(html_data)
    # print(selector)
    # 一次提取
    lis = selector.xpath('//ul[@class="plcCitylist"]/li')
    # print(lis)
    # print(lis)
    # 二次提取
    # if not os.path.exists('/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img'):
    #     os.mkdir('/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img')

    for li in lis:
        '''
        去掉&nbsp(硬空格）;需要在unicode下替换才行  --> u'\xa0'
        '''
        # city_name = li.xpath('./h3/a/text()').get().strip(u'\xa0') 这里可以多条件提取英文名
        city_name = li.xpath('./h3/a/text()').get().replace(u'\xa0', '')
        # print(city_name)
        travel_people = li.xpath('./p[@class="beento"]/text()').get()
        # print(travel_people)
        travel_hot = li.xpath('./p[@class="pois"]/a/text()').getall()
        # print(travel_hot)

        '''！！！这里用列表推导式更方便一些'''
        travel_hot_list = []
        for i in travel_hot:
            new_travel_hot = i.replace('\n', '').strip()  # \n也属于空白，没必要replace，直接strip就行
            travel_hot_list.append(new_travel_hot)
        travel_hot_str = '、 '.join(travel_hot_list)
        travel_hot_str = f'[{travel_hot_str}]'
        # print(travel_hot_list)
        img_url = li.xpath('./p[@class="pics"]//img/@src').get()
        # print(type(img_url))
        # img_content = requests.get(img_url).content
        save_file(city_name, travel_people, travel_hot_str, img_url)


def save_file(cityname, travelpeople, travelhot, imgurl):
    with lock:
        with open('/Users/lujinghan/PycharmProjects/Scrapping/11 多进程与多线程/03 课后作业/01.csv', mode='a',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([cityname, travelpeople, travelhot, imgurl])


def main(url):
    start_time = time.time()

    response = send_requeset(url)

    html_data = response.text

    parse_save_data(html_data)

    '''save_file函数这里不能单独使用，要单独使用parse_save_data函数得使用yield'''
    # save_file(city_name, travel_people, travel_hot_str, img_content)

    end_time = time.time()

    run_time = end_time - start_time
    print('该子线程运行时间：', run_time, '秒')


if __name__ == '__main__':
    start_time = time.time()

    lock = threading.Lock()
    with open('/Users/lujinghan/PycharmProjects/Scrapping/11 多进程与多线程/03 课后作业/01.csv', mode='a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['城市名', '去过的人数', '热门景点', '城市图片url'])

    urls = [f'https://place.qyer.com/china/citylist-0-0-{i}' for i in range(1, 171)]

    for url in urls:
        thread = threading.Thread(target=main, args=(url,))
        thread.start()
        thread_obj = threading.enumerate()
        print('当前运行线程数', thread_obj)

    end_time = time.time()
    print('主线程运行时间：', end_time - start_time)
