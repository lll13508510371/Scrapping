import pprint
import requests


url = 'https://github.com/'


# timeout=1  设置请求时间,单位秒, 超过时间就会报错, 可以通过异常捕获取处理
try:
    response = requests.get(url=url, timeout=0.01)
    print(response.text)
except Exception as e:
    print(e)
    pass


