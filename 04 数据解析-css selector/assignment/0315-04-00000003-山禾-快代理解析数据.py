"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印即可
"""
import time
import parsel
import requests

url = 'https://www.kuaidaili.com/free/inha/1/'

''' 
Referer全部都从同一个页面跳转是合理的，不同for循环提取前一页的页数
但我估计selenium自动化需要，因为它是自动点击，每一页都会点，referer需要
填入上一页的链接 
 '''
headers = {
    'Host': 'www.kuaidaili.com',
    'Referer': f'https://www.kuaidaili.com/free/inha/1/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

#
# response = requests.get(url=url, headers=headers)
# # print(response.status_code)
# print(response.text)

for i in range(4966):
    print(f'---------第{i+1}页数据------------')

    url = f'https://www.kuaidaili.com/free/inha/{i+1}/'

    '''这里不等待请求的话有些页面还没请求到就进行其它的页面请求了'''
    # time.sleep(0.5)
    try:
        response = requests.get(url=url, headers=headers)

        html_data = response.text


        selector = parsel.Selector(html_data)

        ip = selector.css('#list tbody>tr>:nth-child(1)::text').getall()
        port = selector.css('#list tbody>tr>:nth-child(2)::text').getall()
        protocol = selector.css('#list tbody>tr>:nth-child(4)::text').getall()

        data_num = len(ip)

        for j in range(data_num):
            print(ip[j], port[j], protocol[j], sep=' | ')

    except Exception as e:
        pass

'''
可能是 --> 在使用requests库的时候，由于请求失败而由程序本身发送重连连接的速度过快导致产生该错误。
减缓出错时重连的速度可能可以有效地解决这一个问题。(time.sleep)

之前下载图片也有重试超出最大次数的错误，有些图片地址已经改了或者没了，请求重试多少次都没用，用try except 捕捉一下错误
'''
'''
网络不行，爬多了老卡住，要不停的换网络，家里网络不行换vpn的网爬，vpn不行了关掉再用家里的网络，感觉得网线才行
'''