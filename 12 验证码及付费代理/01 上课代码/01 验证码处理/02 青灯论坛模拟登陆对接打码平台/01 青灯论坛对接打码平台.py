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

img_response = session.get(url=img_url)
img_data = img_response.content

with open('yzm.png', mode='wb') as f:
    f.write(img_data)

# # # 手动输入验证码
# code = input('请输入验证码:')
# print(f'您输入的验证码为: {code}')

"""对接打码平台自动识别验证码"""
from img_api import base64_api

result = base64_api('yzm.png', typeid=1001)
print('验证码识别结果:', result)



"""构建登陆的请求"""
login_url = 'http://43.138.139.29:5000/api/private/v1/login'
json_data = {
    "image_code": img_time,  # 图片验证码的时间戳
    "username": "admin",  # 登陆用户名
    "password": "123456",  # 登陆密码
    "captcha_code": result  # 验证码
}
print(json_data)
login_response = session.post(url=login_url, json=json_data)
print(login_response.json())
