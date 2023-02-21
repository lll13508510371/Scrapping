import requests

proxy_response = requests.get('http://134.175.188.27:5010/get')
proxy = proxy_response.json()
print(proxy)

# requests.exceptions.ConnectionError 链接报错

# 服务器：目标数据数据服务器没有 或者识别你的ip发送的请求不正常
# 客户端: 网络环境
# 服务器: 瘫痪  500左右

# 大企业有容灾机制
