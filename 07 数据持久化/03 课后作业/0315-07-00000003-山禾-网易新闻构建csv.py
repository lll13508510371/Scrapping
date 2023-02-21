"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为csv格式
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""
import csv
import requests
import json

url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'

response = requests.get(url=url)

data = response.text
# print(data)
data_str = data.strip('data_callback(').strip(')')
# print(data_list)
data_list = json.loads(data_str)
# pprint.pprint(data_list)
'''
title  
channelname  
docurl  
imgurl  
source  
tlink
'''
rows = [(i['title'], i['channelname'], i['docurl'], i['imgurl'], i['source'], i['tlink']) for i in data_list]
# print(rows)

with open('网易新闻.csv', mode='a', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    '''
    这里可以创建Dicwriter字典写入对象用字典写入
    '''
    csv_writer.writerow(('title', 'channelname', 'docurl', 'imgurl', 'source', 'tlink'))
    for row in rows:
        csv_writer.writerow(row)
