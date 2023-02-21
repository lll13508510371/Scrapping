"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	发送 GET 请求
	
	
	要求：
		1、请求上述网址的数据
		2、按照要求提取以下字段信息
			title、
			picPath、
			playUrl
		提取下来用 print() 函数打印即可
请在下方编写代码
"""
import pprint

import requests

response = requests.get('https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76')
json_data = response.json()  # json() 方法提取出来不的数据会数据在底层经过数据转化
print(json_data)
print(type(json_data))
# pprint.pprint(json_data)

data_list = json_data['data']

for data in data_list:
    title = data['title']
    picPath = data['picPath']
    playUrl = data['playUrl']
    print(title, picPath, playUrl, sep=' | ')