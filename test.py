import json
import random
import re

import parsel
import requests
import time
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

'''
pycharm默认用utf-8解码（在pycharm当中查看文件）
'''

# headers = {
#     'referer': 'https://www.duitang.com/search/?kw=蜡笔小新&type=feed',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }
# url = 'https://www.duitang.com/napi/blogv2/list/by_search/?kw=%E8%9C%A1%E7%AC%94%E5%B0%8F%E6%96%B0&after_id=120&type=feed&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&_=1676133118726'
# query_str_param = {
#     'kw': '蜡笔小新',
#     'after_id': '24',
#     'type': 'feed',
#     'include_fields': 'top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id',
#     '_type': '',
#     '_': str(int(time.time() * 1000))
# }
# response = requests.get(url=url,  params=query_str_param)
# response.encoding = response.apparent_encoding
# print(response)

# print(response.json())
# a = ''
# print(type(a))
#
# a = '{"a": "1"}'
#
# b = json.loads(a)
# print(type(json.loads(a)))
#
# print(json.dumps(b))

# str_1 = '123'
#
# for i in str_1:
#     print(i)
#
# set_1 = {1, 2, 3, 4}
#
# for j in set_1:
#     print(j)
#
# dic_1 = {
#     'a': 1,
#     'b': 2
# }
#
# print(dic_1.items())
# for i in dic_1.items():
#     print(i)
#
# for i, j in dic_1.items():
#     print(i, j)

# a = '1'
# b = '2'
# c = a, b
# d = a + b
# print(c)
# print(d)

# import re
#
# s = "<a target='_blank' href='https://haokan.baidu.com/v?vid=15438469986248172425&sfrom=gaoxiao_new' class='ssr-videoitem-extinfo'>122万次播放 . 2022年07月10日</a>"
#
# s_2 = re.findall(
#     "a target=.*? href='https://haokan.baidu.com/v\?vid=15438469986248172425&sfrom=gaoxiao_new' class='ssr-videoitem-extinfo'>122万次播放 . 2022年07月10日</a>",
#     s, re.S)
#
# print(s_2)

# a = 1
# b = 2
#
# # print(a, b, sep=' | ')
# collection = []
#
# # arr.append(a)
# # arr.append(b)
# #
# # print(arr)
#
''' 
如果是空列表，for 循环进行迭代做任何操作都不会报错
'''

# try:
#     print('123')
#     print('1' + 4)
#
# except Exception:
#     pass
# print()

# import numpy as np
# # np.random
# import requests
# import parsel
#
# headers = {
#     'Cookie': 't=f427923af25aab40f88205f45c51868e; r=5138',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }
# response = requests.get(url='http://www.win4000.com/wallpaper_detail_34370.html', headers=headers)
#
# html_data = response.text
# print(html_data)
# selector = parsel.Selector(html_data)
#
# pics_url_list = selector.xpath('//div[@class="scroll-img-cont "]//li//img/@src').getall()
#
# print(pics_url_list)
# import json
# a = '[1]'
# # c = json.dumps(a)
# # print(c)
# print(type(a))
# e = json.loads(a)
# print(e)
# with open('data_2.json', mode='w', encoding='utf-8') as f:
#     f.write("{'a': '34'}")

# a = 'a'
# print(a > 'b' or 'c')

# print('b' or 'c')
# print(1 > 0 or 'c')

# print(type(1 > 0))
# print('可以')
# print(['可以', 1])
# for i in ['可以', 1]:
#     print(i)
# print("{'可以'：1}")

# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get('https://www.baidu.com')
#
# from selenium.webdriver.common.by import By
#
# By.ID
# print(random.randint(0, 12))

# a = [1, 2, 3, 4, 5]
# for i in range(3):
#     print(a[random.randint(0, len(a))-1])
#     print(len(a))

# print(time.time() * 1000)
# a = []
# print(len(a))
# if 0:
#     print(1)
# else:
#     print(2)

response = requests.get('http://language.chinadaily.com.cn/thelatest/page_1.html')
html_data = response.text
# print(html_data)
selector = parsel.Selector(html_data)
divs = selector.css('.content_left>.gy_box')
#
i = 1
while i < 10:
    next_page = selector.css('.content_left>#div_currpage>.pagestyle::attr(href)').get().split('/')[-1]
    print(next_page)
    page_num = re.findall('.*_(.*?)\..*', next_page)
    print(page_num)
    i += 1
# for div in divs:
#     title = div.css('.gy_box_txt>p:nth-child(1)>a::text').get()
#     introduction = div.css('.gy_box_txt>p:nth-child(2)>a::text').get()
#     '''
#     !!! 二次提取如果只写标签名不需要加.
#     '''
    # img = div.css('a>img::attr(src)').get()
    # print(title, introduction, img)
# a = selector.css('.content_left>.gy_box>a>img::attr(src)').get()
# print(a)

print('2' < '11')
print(2 < 11)
# next_page = 'page_1.html'
# page_num = re.findall('.*_(.*?)\..*', next_page)[0]
# print(type(page_num))
