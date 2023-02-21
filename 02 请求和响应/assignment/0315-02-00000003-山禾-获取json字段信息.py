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
import requests
import pprint

response = requests.get('https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76')

# html_data = response.text --> str

data = response.json()
print(data)

for i in data['data']:
    print(i['title'])
    print(i['picPath'])
    print(i['playUrl'])
