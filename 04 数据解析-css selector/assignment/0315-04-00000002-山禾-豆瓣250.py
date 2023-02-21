"""
    使用 css 选择器将豆瓣250 十页的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250

    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
	
	提取出来print（）打印即可
"""
import time

import parsel
import requests
requests.packages.urllib3.disable_warnings()

url = 'https://movie.douban.com/top250?'


def get_query_params(i):
    query_params = {
        'start': str(i * 25),
        'filter': ''
    }

    return query_params


def get_proxy():
    """获取代理函数"""
    json_data = requests.get(url='http://demo.spiderpy.cn/get/').json()
    # print(json_data)
    proxy = json_data['proxy']
    # print(proxy)

    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    # print(proxies)
    return proxies


# get_proxy()

headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

for i in range(10):
    print(f'第{i+1}页数据')

    try:
        time.sleep(1)

        response = requests.get(url=url, headers=headers, params=get_query_params(i), verify=False)

        html_data = response.text
        # print(html_data)
        # print(response.status_code)
        # --> 418 拒绝冲泡咖啡因为我是个茶壶，被服务器识别出是机器
        # --> HTTP 418 I'm a teapot 客户端错误响应代码表示服务器拒绝冲泡咖啡，因为它是个茶壶。
        selector = parsel.Selector(html_data)
        '''
        title（电影名）
        info（导演、主演、出版时间）
        score（评分）
        follow（评价人数）
        '''
        # 统计数据数量
        film_num = len(selector.css('.hd>a>:nth-child(1)::text').getall())

        all_title = selector.css('.hd>a>:nth-child(1)::text').getall()
        all_info = selector.css('.bd>p:nth-child(1)::text').getall()
        all_score = selector.css('.rating_num::text').getall()
        all_follow = selector.css('.star>:nth-child(4)::text').getall()
        # print(all_title)
        # print(len(all_info))
        # print(all_score)
        # print(all_follow)

        for j in range(film_num):

            info_part_1 = all_info[j * 2].strip()
            '''strip默认去除空白的字符串（不是空字符串）'''

            info_part_2 = all_info[j * 2 + 1].strip()
            # print(info_part_1)
            info = info_part_1 + ' | ' + info_part_2
            # print(info)
            print(all_title[j], all_score[j], all_follow[j], info, sep=' | ')

    except Exception as e:
        pass

'''
用家里面的网被豆瓣识别ip异常需要登陆验证，换vpn网就能爬取到
ip--> 相当于家🏠，从防火墙内的🏠（我的ip)连接到网站服务器 
      和换vpn从防火墙外的香港的🏠（另一个ip）连接到网站服务器
'''