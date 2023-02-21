import csv

import requests
import parsel

# 1.找请求地址
url = 'https://m.maoyan.com/asgard/board/4'
headers = {
    # 'Cookie': 'iuuid=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; _lxsdk_cuid=1803c6fc140c8-03e4923d825316-1734337f-1fa400-1803c6fc140c8; _lxsdk=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; webp=true; featrues=[object Object]; _lxsdk_s=185aae34498-06d-faa-0fa%7C%7CNaN; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1673263907,1673609299; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1673609299',
    # 'Host': 'm.maoyan.com',
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
divs = selector.css('.board-card.clearfix')  # 提取到所有的div标签

with open('猫眼-列表.csv', mode='a', encoding='utf-8', newline='') as f:
    # 没有列表写入表头的方法  针对列表写入csv, 表头可以用普通文本的方式写入
    f.write('电影名字,主演,上映时间,评分\n')
    csv_write = csv.writer(f)

    for div in divs:
        title = div.css('.title::text').get()
        actors = div.css('.actors::text').get()
        date = div.css('.date::text').get()
        number = div.css('.number::text').get()
        print(title, actors, date, number)

        csv_write.writerow((title, actors, date, number))


