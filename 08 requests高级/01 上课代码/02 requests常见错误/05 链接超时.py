import requests

# timeout 超出这个时间就报错
proxy_response = requests.get('http://134.175.188.27:5010/get', timeout=0.01)
proxy = proxy_response.json()
print(proxy)

"""
ConnectTimeout 链接超时
"""