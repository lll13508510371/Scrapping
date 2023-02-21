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


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

"""请求验证码图片保存"""
img_time = get_time()
img_url = 'http://43.138.139.29:5000/login/captcha?image_code=' + img_time
print(img_url)

img_response = requests.get(url=img_url)
img_data = img_response.content

with open('yzm.png', mode='wb') as f:
    f.write(img_data)

# 手动输入验证码
code = input('请输入验证码:')
print(f'您输入的验证码为: {code}')

"""构建登陆的请求"""
login_url = 'http://43.138.139.29:5000/api/private/v1/login'
'''虽然说"image_code"是int，但传str是没有问题的'''
json_data = {
    "image_code": img_time,  # 图片验证码的时间戳
    "username": "admin",  # 登陆用户名
    "password": "123456",  # 登陆密码
    "captcha_code": code  # 验证码
}
print(json_data)
login_response = requests.post(url=login_url, json=json_data)
print(login_response.json())


"""这两次请求默认情况下是单次请求（可以理解为不同的人请求）"""
# 可以通过代码构建请求的关联性--> 会话维持

"""登陆成功后请求用户页面"""
user_url = 'http://43.138.139.29:5000/'
user_response = requests.get(url=user_url)
with open('无会话维持用户页面.html', mode='w', encoding='utf-8') as f:
    f.write(user_response.text)
    
'''
发现post一般不加headers --> 还是有加的，Uniq和Coniun里面都加了
'''
'''
没有会话维持，会重定向到登陆页网址（url)
无会话维持，就相当于第一次一个人请求，第二次是第二个人请求，服务器不确定你是不是本人，就不让你登陆
或者可以理解成请求之间没有联系，第一次请求相当于是一个人，里面没有cookie，会让你进行登陆操作，第二次请求相当于是第二个人，
里面还是没有cookie，http://43.138.139.29:5000/还是会跳转到login页面
'''


