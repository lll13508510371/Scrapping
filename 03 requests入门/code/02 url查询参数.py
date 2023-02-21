# https://pic.sogou.com/pics?query=%E9%A3%8E%E6%99%AF&mood=7&dm=0&mode=1

# 在http协议中不支持中文编码显示
# 如果地址中有中文, 会经过url编码, 形式: 由 百分号 + 字母 + 数据 组成

"""
查询参数: 指的是地址中 ? 后面的内容

? 前面是请求地址, 后面是一系列的查询参数
& 隔开每一个查询参数
所有的查询参数都数据二值型数据(mode 7)
"""

import requests

params = {
    'mode': '1',
    'mood': '7',
    'query': '风景',
    'dm': '0',
}

url = 'https://pic.sogou.com/pics'



# ? 可加可不加 ？就是用来分隔url 和 查询参数，所以加不加都行，后面如果忘了就加上？怎么都不会错
response = requests.get(url=url, params=params)
print(response.request.url)

"""url编码问题"""
# requests.utils.quote 对中文进行url编码
print(requests.utils.quote('风景'))
# requests.utils.unquote  url解码-->将编码转换成中文
print(requests.utils.unquote('%E9%A3%8E%E6%99%AF'))
