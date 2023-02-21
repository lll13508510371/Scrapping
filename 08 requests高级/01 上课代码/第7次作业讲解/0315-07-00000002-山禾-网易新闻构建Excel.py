"""
目标站点: https://news.163.com/

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
import re
import openpyxl
import requests


url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'

response = requests.get(url=url)
data = response.text
print(data)

result = re.findall('data_callback\((.*?)\)', data, re.S)[0]
print(result)

data_list = json.loads(result)
print(data_list)

work = openpyxl.Workbook()
sheet = work.active

for data_ in data_list:
    title = data_['title']
    channelname = data_['channelname']
    docurl = data_['docurl']
    imgurl = data_['imgurl']
    source = data_['source']
    tlink = data_['tlink']
    print(title, channelname, docurl, imgurl, source, tlink, sep=' | ')
    sheet.append([title, channelname, docurl, imgurl, source, tlink])

work.save('wangyi新闻.xlsx')
