"""
表情包爬取
将此页面下的前五页图片全部获取下来：https://www.biaoqingbao.net/gaoxiao/
"""
"""请下下方开始编写代码"""

import requests
import re

'''https://www.biaoqingbao.net/gaoxiao/page_2.html'''
for j in range(1, 6):
    response = requests.get(
        f'https://www.biaoqingbao.net/gaoxiao/page_{j}.html')

    html_data = response.text

    '''
    <div class="post_left"><a href=.*? target="_blank"><img class="waitpic" src=.*? data-original=(.*?) alt=.*? ><div class="cx-cover"><img src=.*? width=.*?height=.*?></div></a></div><div class="post_right">
    '''

    content = re.findall(
        r'(https:[^\s]*?(jpg|gif))"',
        html_data, re.S)

    for i in content:
        url = i[0]
        response = requests.get(url)
        data = response.content
        file_name = i[0].split('/')[-1]
        with open(file_name, mode='wb') as f:
            f.write(data)

# response2 = requests.get(content[0].strip('"'))
#
# # print(content[0].strip('"').split('/')[-1])
#
# file_name = content[0].strip('"').split('/')[-1]

# data = response2.content

'''
这样只能爬一张图   <div class="post_left"><a href=".*?" target="_blank"><img class="waitpic" src=".*?" data-original="(.*?)" alt=".*?" ><div class="cx-cover"><img src=".*?" width=".*?" height=".*?"></div></a></div><div class="post_right">
'''

# with open(file_name, mode='wb') as f:
#     f.write(data)
