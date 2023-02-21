"""
    目标网址: https://place.qyer.com/china/citylist-0-0-1/
    
    需求:
        1、用xpath采集数据
        2、采集以下信息
            city_name   # 城市名
            travel_people  # 去过的人数
            travel_hot    # 热门景点
            img_url  # 城市图片url
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""
import os

import parsel
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

html_data = requests.get('https://place.qyer.com/china/citylist-0-0-1/', headers=headers).text
# print(html_data)
selector = parsel.Selector(html_data)
# print(selector)
# 一次提取
lis = selector.xpath('//ul[@class="plcCitylist"]/li')
# print(lis)
# print(lis)
# 二次提取
if not os.path.exists('/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img'):
    os.mkdir('/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img')

for li in lis:
    '''
    去掉&nbsp;需要在unicode下替换才行  --> u'\xa0'
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
    travel_hot_str = ','.join(travel_hot_list)
    # print(travel_hot_list)
    img_url = li.xpath('./p[@class="pics"]//img/@src').get()
    # print(type(img_url))
    content = requests.get(img_url).content

    with open(os.path.join('/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img', city_name + '.png'),
              mode='wb') as f:
        f.write(content)

    print(city_name, travel_people, travel_hot_str, sep=' | ')
