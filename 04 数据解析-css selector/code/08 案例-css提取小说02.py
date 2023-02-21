import parsel
import requests

url = 'http://www.biqugse.com/28893/51265857.html'
response = requests.get(url=url)
html_data = response.text
print(html_data)  # 在数据解析前, 一定要确认数据是请求到了的

"""解析数据"""
# 1.转类型
selector = parsel.Selector(html_data)

# 2.解析数据
# name = selector.css('h1').getall()
name = selector.css('.bookname h1::text').getall()
print(name)

result = selector.css('#content::text').getall()
print(result)
result_str = ''.join(result)
# print(''.join(result))
result_2 = result_str.replace('\n', '').replace('\t', '')
print(result_2)
result = selector.css('#content::attr(id)').getall()
print(result)
