import requests

headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/top250',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://movie.douban.com/top250', headers=headers)
html_data = response.text

# 响应体的常见方法和属性
print(response.text)  # # 获取响应体的文本数据  str
print(response.content)  # # 获取响应体的二进制数据
# print(response.json())  # # 获取响应体的json数据, 如果响应体对象里面的数据不是json数据, 使用json()提取就会报错 --> simplejson.errors.JSONDecodeError

print(response.headers)  # # 查看响应体的响应头信息
print(response.encoding)  # # 指定响应体编码
print(response.apparent_encoding)  # # 自动识别响应体编码, 常用于乱码的网站
print(response.cookies)  # 获取响应体的 cookies 字段信息, 得到的是 RequestsCookieJar 对象

# print(response.cookies.get_dict())
print(response.url)  # # 获取响应体的url地址
print(response.status_code)  # # 获取响应体状态码