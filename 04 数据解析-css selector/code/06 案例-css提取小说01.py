import parsel
import requests

url = 'http://www.biqugse.com/28893/51265857.html'
response = requests.get(url=url)
html_data = response.text
print(html_data)  # 在数据解析前, 一定要确认数据是请求到了的

"""解析数据"""
# 1.转类型
selector = parsel.Selector(html_data)
print(selector)
# 2.解析数据
# name = selector.css('h1').getall()
name = selector.css('.bookname h1').get()
print(name)

result = selector.css('#content').getall()
result_2 = selector.css('#content').get()
print(result)
print(result_2)
"""
数据解析以代码获取的数据为准

通过代码保存html文件, 然后用浏览器打开, 在打开的页面写语法
"""