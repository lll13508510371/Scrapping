"""
按照以下网址爬取小说。爬取《剑来》前面五章的小说数据,分别保存在不同的txt文件下

-- 网址： https://www.bige7.com/book/1031/

请下下方开始编写代码
"""
import requests
import re

response = requests.get('https://www.bige7.com/book/1031/')

html_data = response.text

'''<dd><a href =(.*?)>.*?</a></dd>'''
results = re.findall('<dd><a href =(.*?)>.*?</a></dd>', html_data, re.S)

# print(results)

# print(result[0].strip('"'))
url1 = 'https://www.bige7.com'

for result in results[:5]:
    # print(result.strip('"'))
    response1 = requests.get(url1 + result.strip('"'))
    html_data1 = response1.text
    name = url1 + result
    file_name = name.split('/')[-1].strip('"')
    all_content = re.findall(
        '<div id="chaptercontent" class=".*?">(.*?)<p class="readinline">.*?</p></div>',
        html_data1, re.S)

    content = all_content[0].replace('<br /><br />', '\n\n').replace(
        '\u3000\u3000',
        '')
    # print(content)
    # print(file_name)
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(content)
'''
<div id="chaptercontent" class=".*?">(.*?)<p class="readinline">.*?</p></div>
'''
