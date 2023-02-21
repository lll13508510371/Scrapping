# requests 是数据请求的模块, 可以指定数据地址, 请求数据结果,  是第三方模块
import requests

'''
# Response 响应体对象(通过requests模块发送请求, 服务器给我们响应的一个对象)
# get  是一种请求方式
# 静态网页都是用get来请求
'''
response = requests.get('https://www.baidu.com/')
print(response)

# 对象, 就具有对象的属性和方法
# .text 获取 Response 对象的文本内容(response响应体属性)
print(response.text)

"""
爬虫项目实现的步骤:

1. 找数据对应的地址(文本 图片 视频 音频), 网页性质的分析 <静态网页/动态网页>
2. 请求地址, 获取地址对相应的数据<js css 图片 视频数据  html  音频数据>
3. 数据筛选, 数据解析, 提取需要的数据, 剔除不要的数据
4. 保存数据(本地, 数据库)


1. 找地址
2. 请求地址
3. 解析数据
4. 保存数据
"""
