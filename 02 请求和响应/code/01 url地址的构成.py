import os

import requests
import re


response = requests.get('https://www.bqg70.com/book/1031/1.html')

"""
https://www.bqg70.com.cn/book/1031/1.html

https://        请求协议的类型(http/https) 超文本传输协议
www             服务器的名字  www(world wide web) 万维网; mail(邮箱服务器名字)
bqg70.com.cn    域名<重点>
/               服务器的根路径
book/1031/1.html  服务器中数据的资源位置, 类似于电脑的盘符路径

https://www.bqg70.com.cn/book/1031/1.html   url<统一资源定位符>地址  / ip 接口
"""

