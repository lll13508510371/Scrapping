"""
    使用 css 选择器将豆瓣250 十页的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250

    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
	
	提取出来print（）打印即可
"""

import requests
import parsel

for page in range(0, 226, 25):
    print('--------------------------------------')
    # 1.找请求地址
    url = f'https://movie.douban.com/top250?start={page}&filter='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    # 2.发送请求
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    html_data = response.text
    print(html_data)  # 打印请求到的数据, 查看数据是已经请求到了

    # 3.数据解析
    # 3.1 转换数据类型
    selector = parsel.Selector(html_data)
    # 3.2 解析数据-->二次提取
    lis = selector.css('.grid_view>li')  # 提取到所有的li标签
    print(lis)
    print(len(lis))

    for li in lis:
        title = li.css('.title:nth-child(1)::text').get()
        info = li.css('.bd p:nth-child(1)::text').getall()
        info_2 = ' | '.join([i.strip().replace('\xa0', '') for i in info])

        score = li.css('.rating_num::text').get()
        people = li.css('.star>span:nth-child(4)::text').get()
        print(info_2)
