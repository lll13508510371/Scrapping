

"""
账号: mb51222353
密码: 123456..
"""
import requests

"""请求个人中心页面保存数据"""
my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response = requests.get(url=my_home_url, headers=headers)
print(response.text)
print(response.status_code)

with open('无会话维持用户页面.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)


# 只有登陆后才有个人中心页面请求的权限, 我们需要做模拟登陆
#
#  使用登陆的状态请求个人中心页面
