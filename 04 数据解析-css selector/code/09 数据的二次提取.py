import parsel
import requests

url = 'http://www.biqugse.com/28893/'
response = requests.get(url=url)
html_data = response.text
print(html_data)  # 在数据解析前, 一定要确认数据是请求到了的

"""解析数据"""
selector = parsel.Selector(html_data)

# 第一次提取: 图区所有符合条件的标签
dd_s = selector.css('#list>dl>dd')  # 提取所有的dd标签
print(dd_s)
print(len(dd_s))

# 二次提取, 当一个标签对象需要多次提取的时候最好用二次提取的方式
# 对象就有对象的属性和方法
for dd in dd_s:
    title = dd.css('a::text').get()
    href = dd.css('a::attr(href)').get()
    print(title, href)

