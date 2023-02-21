import requests
import parsel



# 1.找请求地址
url = f'https://movie.douban.com/top250?start=0&filter='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# 2.发送请求
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
# print(html_data)  # 打印请求到的数据, 查看数据是已经请求到了

# 3.数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)
# 3.2 解析数据-->二次提取
lis = selector.xpath('//ol[@class="grid_view"]/li')  # 提取到所有的li标签
# print(lis)
# print(len(lis))

for li in lis:
    title = li.xpath('.//span[@class="title"][1]/text()').get()
    info = li.xpath('.//div[@class="bd"]/p[1]/text()').getall()
    info = ''.join([i.strip().replace('\xa0', ' ') for i in info])

    score = li.xpath('.//span[@class="rating_num"]/text()').get()
    people = li.xpath('.//div[@class="star"]/span[4]/text()').get()
    print(people)