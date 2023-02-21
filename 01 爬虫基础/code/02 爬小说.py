import requests
import re  # 内置模块, 正则表达式解析模块

response = requests.get('https://www.bqg78.com/book/1031/1.html')
html_data = response.text
# print(html_data)


# 解析提取数据
# re.findall(解析规则, 解析数据, 解析模式)
"""
<div id="chaptercontent" class=".*?">(.*?)<p class="readinline">.*?</p></div>
"""
result = re.findall(
    '<div id="chaptercontent" class=".*?">(.*?)<p class="readinline">.*?</p></div>',
    html_data,
    re.S)

# print(result)

content = result[0].replace('<br /><br />', '\n\n').replace('\u3000\u3000', '')
print(content)

# with open('a.txt', mode='w', encoding='gbk') as f:
#     f.write(content)
'''
pycharm默认utf-8解码,gbk编码在pycharm打开会乱码
'''