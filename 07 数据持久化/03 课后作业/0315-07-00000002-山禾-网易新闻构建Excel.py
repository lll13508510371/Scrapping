"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为 Excel 表格
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""
import json
import pprint
import openpyxl
import requests

url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'

''' get没有qurey parameter参数，是post的 '''
response = requests.get(url=url)

data = response.text
# print(data)
'''这里可以用re.findall，还没有建立这个意识，习惯性的想着用strip'''
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

workbook_1 = openpyxl.Workbook()
sheet_1 = workbook_1.active

sheet_1.append(('title', 'channelname', 'docurl', 'imgurl', 'source', 'tlink'))

for row in rows:
    sheet_1.append(row)

workbook_1.save('网易新闻.xlsx')
