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

with open('猫眼-字典.csv', mode='a', encoding='utf-8', newline='') as f:
    # 创建字典写入对象
    csv_write = csv.DictWriter(f, fieldnames=['title', 'actors', 'date', 'number'])
    csv_write.writeheader()  # 写入表头

    for div in divs:
        title = div.css('.title::text').get()
        actors = div.css('.actors::text').get()
        date = div.css('.date::text').get()
        number = div.css('.number::text').get()
        print(title, actors, date, number)

        d = {'title': title, 'actors': actors, 'date': date, 'number': number}

        csv_write.writerow(d)

'''
发现python例如line之类的方法有区分单复数 e.g. writerow() writerows()
'''


# csv 写入表头, 仅针对字典数据提供了方法
