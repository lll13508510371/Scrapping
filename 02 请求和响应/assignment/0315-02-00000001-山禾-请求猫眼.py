"""
	目标地址：https://m.maoyan.com/board/4
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		
请在下方编写代码
"""


''' 1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息 '''

import requests
import re

headers = {
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',

}
'''
这里需要的就是user-agent，不一定需要全部主要的请求头，具体网站具体分析需要哪些请求头
'''
response = requests.get('https://m.maoyan.com/asgard/board/4', headers=headers)
'''
<div class="info"><h3 class="title">.*?</h3><div class=.*?>
徐峥,周一围,王传君</div><div class="cat"></div><div class="date">2018-07-05</div></div><div class="right extra-right"><div><span class="number">9.6</span>分</div>
<h3 class="title">(.*?)</h3><div class="actors">(.*?)</div><div class="cat"></div><div class="date">(.*?)</div></div><div class="right extra-right"><div><span class="number">(.*?)</span>(.*?)</div>
'''
html_data = response.text
print(response.text)

# title_data = re.findall('<div class="info"><h3 class="title">(.*?)</h3><div class=.*?>', html_data, re.S)
#
# actor_data = re.findall('<div class="actors">(.*?)</div><div class=.*?">', html_data, re.S)
#
# date_data = re.findall('<div class=".*?"></div><div class="date">(.*?)</div></div><div class=.*?>', html_data, re.S)
#
# number_data = re.findall('<div><span class=(.*?)>.*?</span>(.*?)</div>', html_data, re.S)

all_data = re.findall(
    '<h3 class="title">(.*?)</h3><div class="actors">(.*?)</div><div class="cat"></div><div class="date">(.*?)</div></div><div class="right extra-right"><div><span class="number">(.*?)</span>(.*?)</div>',
    html_data, re.S)

'''
!!! 如果正则得不到全部想要的数据，可以用for循环然后用str的replace()把不想要的数据转换成''，当然数据要么是str要么str()
'''

# print(title_data)
# print(actor_data)
# print(date_data)
# print(number_data)
print(all_data)

list_1 = []
for content in all_data:
    dic = {
        '电影名字': content[0],
        '主演': content[1],
        '上映时间': content[2],
        '评分': content[3] + content[4]
    }
    list_1.append(dic)

print(list_1)

''' 2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）'''
'''
有就add:
1.Host
2.User-Agent
3.Referer
如果不能请求到add:
4.Cookie

'''
