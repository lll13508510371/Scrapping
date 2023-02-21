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


with open('wangyi新闻2.csv', mode='a', encoding='utf-8', newline='') as f:
    '''字典写入对象针对字典数据写入'''
    csv_write = csv.DictWriter(f, fieldnames=['title','channelname','docurl','imgurl','source','tlink'])
    csv_write.writeheader()

    for data_ in data_list:
        title = data_['title']
        channelname = data_['channelname']
        docurl = data_['docurl']
        imgurl = data_['imgurl']
        source = data_['source']
        tlink = data_['tlink']
        print(title, channelname, docurl, imgurl, source, tlink, sep=' | ')
        d = {'title': title, 'channelname': channelname, 'docurl': docurl, 'imgurl': imgurl, 'source': source, 'tlink': tlink}

        csv_write.writerow(d)

# with open('wangyi新闻.csv', mode='a', encoding='utf-8', newline='') as f:
#     f.write('新闻标题,新闻分类,资源地址,图片地址,资源,链接\n')
#     csv_write = csv.writer(f)
#
#     for data_ in data_list:
#         title = data_['title']
#         channelname = data_['channelname']
#         docurl = data_['docurl']
#         imgurl = data_['imgurl']
#         source = data_['source']
#         tlink = data_['tlink']
#         print(title, channelname, docurl, imgurl, source, tlink, sep=' | ')
#
#         csv_write.writerow([title, channelname, docurl, imgurl, source, tlink])

