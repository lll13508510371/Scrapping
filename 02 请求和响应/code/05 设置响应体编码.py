# http://www.biqu5200.net/0_111/75039.html


import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://epe.xjtu.edu.cn/xwzx/xygg.htm')

"""在响应体数据出现乱码的时候用"""
# response.encoding = 'utf-8'  # 手动指定响应体编码
response.encoding = response.apparent_encoding  # apparent_encoding 自动识别响应体编码

html_data = response.text
print(html_data)
print(response.encoding)