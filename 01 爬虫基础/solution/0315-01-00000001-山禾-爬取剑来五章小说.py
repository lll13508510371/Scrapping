"""
按照以下网址爬取小说。爬取《剑来》前面五章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.bige7.com/book/1031/

请下下方开始编写代码
"""
# 爬取小说-->爬取的一章小说数据
import os

import requests
import re


url = 'https://www.bqg70.com/book/1031/'
response = requests.get(url)
html_data = response.text
print(html_data)

"""
<dd><a href ="/book/1031/1.html">第一章 惊蛰</a></dd>
<dd><a href ="(.*?)">.*?</a></dd>
<dd><a href =(.*?)>.*?</a></dd>
"""
result = re.findall('<dd><a href ="(.*?)">.*?</a></dd>', html_data, re.S)
# print(result[:5])

if not os.path.exists('剑来'):
    os.mkdir('剑来')

for res in result[:5]:
    # 拼接完整地址
    all_url = 'https://www.bqg70.com' + res
    # print(all_url)

    """上课的代码逻辑"""
    response_2 = requests.get(all_url)
    html_data_2 = response_2.text
    result_2 = re.findall('<div id="chaptercontent" class=".*?">(.*?)<p class="readinline">.*?</p></div>',
                        html_data_2,
                        re.S)

    contend = result_2[0].replace('<br /><br />', '\n\n').replace('\u3000\u3000', '')

    # 解析章节名:用于保存文件, 作为文件名
    file_name = re.findall('<h1 class="wap_none">(.*?)</h1>', html_data_2, re.S)[0]


    with open('剑来\\' + file_name + '.txt', mode='w', encoding='utf-8') as f:
        print('正在保存', file_name)
        f.write(contend)
        print('保存完成:', file_name)
# \ --> 转义字符 -->再加一个\把转义字符\转换为普通字符
# /
'''
'正在保存', file_name都print出来了说明print已经结束，已经开始执行f.write(contend)写入文件
'''