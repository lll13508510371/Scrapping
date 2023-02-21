import pprint
import requests

url = 'http://github.com/'

# requests会自动重定向, allow_redirects=False --> 阻止重定向
response = requests.get(url=url, allow_redirects=False)
print(response.status_code)
'''
极少数时候，需要的数据是重定向之前的数据
'''