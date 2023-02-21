import requests


count = 0
try:
    count += 1
    proxy_response = requests.get('http://134.175.188.27:5010/get', timeout=0.01)
    proxy = proxy_response.json()
    print(proxy)

except Exception as e:
    try:
        count += 1
        proxy_response = requests.get('http://134.175.188.27:5010/get', timeout=0.01)
        proxy = proxy_response.json()
        print(proxy)
    except:
        pass


print(count)

"""
对于报错我们可以用异常捕获

如果对于请求异常的情况, 但需要异常重试直到成功为止, 那就需要用到函数递归
"""