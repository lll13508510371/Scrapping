

"""
账号: mb51222353
密码: 123456..
"""
import requests


"""模拟登陆"""
headers = {
    'Host': 'passport3.pcbaby.com.cn',
    'Origin': 'https://my.pcbaby.com.cn',
    'Referer': 'https://my.pcbaby.com.cn/login.jsp?return=https%3A//www.pcbaby.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

session = requests.Session()

data = {
    'return': 'https://www.pcbaby.com.cn/',
    'bindUrl': 'https://my.pcbaby.com.cn/passport/bindMobile.jsp?return=https://www.pcbaby.com.cn/',
    'username': 'mb51222353',
    'password': '123456..',
    'auto_login': '30',
    'checkbox': 'on',
}

login_url = 'https://passport3.pcbaby.com.cn/passport3/passport/login_ajax_do_new.jsp?req_enc=UTF-8'
login_response = session.post(url=login_url, headers=headers, data=data)
print(login_response.json())
print(login_response.status_code)



"""请求个人中心页面保存数据"""
my_home_url = 'https://my.pcbaby.com.cn/user/adminIndex.jsp'
# 会话也会维持请求头字段
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response = session.get(url=my_home_url)
print(response.text)
print(response.status_code)

with open('有会话维持用户页面.html', mode='w', encoding='gb2312') as f:
    f.write(response.text)


# 只有登陆后才有个人中心页面请求的权限, 我们需要做模拟登陆
# 使用登陆的状态请求个人中心页面

# 在登陆的时候, 用户名和密码等一些用户信息一般不会以明文方式传递, 如果加密了, 需要逆向解密<js>
