import requests

headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/top250',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://movie.douban.com/top250', headers=headers)
html_data = response.text

# response.request 查看请求体
print(response.request.url)  # # 查看请求体中 url 地址
print(response.request.headers)  # # 查看请求体中请求头信息, requests模块在请求时,会自动带上常见的请求字段
print(response.request.method)  # 查看请求体中请求方法
