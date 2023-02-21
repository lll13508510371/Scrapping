# http://demo.spiderpy.cn/get/  代理接口
import requests

"""
代理形式
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
"""


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

get_proxy()



url = 'https://www.baidu.com/'

# proxies关键字 ————》使用代理发送请求
# 如果代理不可用就会报错， requests.exceptions.ProxyError
response = requests.get(url=url, proxies=get_proxy())
print(response.text)

'''
每一次的request请求都属于一个连接（有些时候会有超出最大连接数的提示，浏览器有些时候会针对一个ip限制连接次数）
'''