import pprint
import requests

requests.packages.urllib3.disable_warnings()  # 忽略证书认证引发的警告

url = 'https://data.stats.gov.cn/'

# verify=False 使用requests模块发送请求的时候,不验证ca证书,默认会验证(verify=True)
response = requests.post(url=url, verify=False)
pprint.pprint(response.text)

"""
SSL CA 证书
requests模块请求会默认验证证书, 没有证书会报错 requests.exceptions.SSLError
"""
