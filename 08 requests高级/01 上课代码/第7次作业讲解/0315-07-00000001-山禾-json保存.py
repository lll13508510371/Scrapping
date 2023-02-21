"""
	目标网址：https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76
	
	要求：
		1、请求上述网址的数据
		2、把获取到的数据保存到json文件中
            文件命名: data.json
            需要在文件中看到json字符串
			
请在下方编写代码
"""
import json

import requests

response = requests.get(url='https://www.ku6.com/video/feed?pageNo=0&pageSize=40&subjectId=76')

json_str = response.json()
# txt = response.text
print(json_str)
print(type(json_str))

# json 数据的序列化操作
data_str = json.dumps(json_str)
with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(data_str)