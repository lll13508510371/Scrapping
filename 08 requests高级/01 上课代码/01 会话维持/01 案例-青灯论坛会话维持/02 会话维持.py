"""
时间戳: 格林威治时间 1970年1月1日0时0分0秒 到 目前 为止所消耗的时间数
    秒级时间戳: 10位数字
    毫秒级时间戳: 13位数字
    微秒级时间戳: 16位数字
"""

import time

import requests


def get_time():
    """获取时间戳的函数"""
    now_time = str(int(time.time() * 1000))
    # print(now_time)
    # print(type(now_time))
    return now_time

# 创建一个会话维持对象
session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

"""请求验证码图片保存"""
img_time = get_time()
img_url = 'http://43.138.139.29:5000/login/captcha?image_code=' + img_time
print(img_url)

img_response = session.get(url=img_url, headers=headers)
img_data = img_response.content

with open('yzm.png', mode='wb') as f:
    f.write(img_data)

# 手动输入验证码
code = input('请输入验证码:')
print(f'您输入的验证码为: {code}')

"""构建登陆的请求"""
login_url = 'http://43.138.139.29:5000/api/private/v1/login'
json_data = {
    "image_code": img_time,  # 图片验证码的时间戳
    "username": "admin",  # 登陆用户名
    "password": "123456",  # 登陆密码
    "captcha_code": code  # 验证码
}
print(json_data)
login_response = session.post(url=login_url, json=json_data)
print(login_response.json())


"""这两次请求默认情况下是单次请求"""
# 可以通过代码构建请求的关联性--> 会话维持
# 会话维持作用: 构建请求之间的关联性, 保证一个会话是一个用户发送的请求

"""登陆成功后请求用户页面"""
user_url = 'http://43.138.139.29:5000/'
'''会话保持，前面有headers，会保持了前面的headers，所以第二次就不用加了'''
user_response = session.get(url=user_url)
with open('无会话维持用户页面2.html', mode='w', encoding='utf-8') as f:
    f.write(user_response.text)

'''
得到的是html文件（静态数据），所以界面很简陋，很多都是动态数据，没有被渲染出来
'''
# 用会话维持把整个登陆状态维持下来了

# 一个网站只有登陆后才可以采集到数据, 登陆的请求和其他请求默认没联系,
# 通过会话维持<用户状态>可以构建登陆后的请求联系

'''
没有会话维持，会重定向到登陆页网址（url)
无会话维持，就相当于第一次是一个人请求，第二次是第二个人请求，服务器不确定你是不是本人，就不让你登陆
'''


