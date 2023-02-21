import requests

url = 'https://www.pcbaby.com.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

response = requests.get(url=url, headers=headers)

# response.encoding = response.apparent_encoding  # 自动识别响应体编码
response.encoding = 'gb2312'  # 自动识别响应体编码
print(response.text)

# 常见编码: gbk, gb2312, gb18030
        #  utf-8,    utf-8-sig  带兼容性的编码格式--> 可以兼容表情符号
        
        