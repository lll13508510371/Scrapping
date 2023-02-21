import requests

headers = {
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/top250',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://movie.douban.com/top250', headers=headers)
html_data = response.text

print(response.status_code)  # # 获取响应体状态码

"""
100 - 199   表示服务器已经成功接收到了请求
200 - 299   表示请求成功  200  206  
300 - 399   重定向(你需要请求的一个资源已经移动到了另外一个位置) 302  306
400 - 499   客户端发送的请求地址在服务器中不到数据  403  404
500 - 599   服务器出现了错误, 是服务器的问题   503  500

状态码仅供参考
"""