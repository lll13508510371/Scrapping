# https://movie.douban.com/top250


import requests

# 将所有的请求头构建成一个字典, 字典中键值对构建好
headers = {
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Accept-Language': 'zh-CN,zh;q=0.9',
    #'Cache-Control': 'no-cache',
    #'Connection': 'keep-alive',
    #'Cookie': 'bid=JOjnHzNKNdU; __gads=ID=390a3a70609550e8-22df6781f5d10053:T=1649854444:RT=1649854444:S=ALNI_MZfvUIHFs1pOYgYSuPbsvh7fVT9Yw; ll="118267"; _vwo_uuid_v2=D9BE563CAF8DB68077925251DB19E9857|7ec7c5b6350ccfad2f138472e47a6641; _ga=GA1.2.1895635950.1649854444; gr_user_id=9841cb26-ad30-4da9-9fad-006c711b218f; __yadk_uid=u5mrwOVUZy3PATAVm4vE63U7vqrPrxRl; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1673010786%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D0_d3rrr64nrwzPvaRHFMlzBv4mR5boDBQJXBo214ZpEMMM45jDdNadH87pmCzaLj%26wd%3D%26eqid%3Def69e7d8000716010000000663b81e60%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1895635950.1649854444.1672836940.1673010786.28; __utmb=30149280.0.10.1673010786; __utmc=30149280; __utmz=30149280.1673010786.28.22.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.913704788.1649854444.1672836940.1673010786.28; __utmb=223695111.0.10.1673010786; __utmc=223695111; __utmz=223695111.1673010786.28.22.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __gpi=UID=0000059a569b8b1b:T=1653051309:RT=1673010787:S=ALNI_MboLjGTnG9YzoGaau8maDJk8dhE7A; _pk_id.100001.4cf6=5a00c88162b3f1ff.1649854444.28.1673011123.1672836939.',
    'Host': 'movie.douban.com',
    #'Pragma': 'no-cache',
    'Referer': 'https://movie.douban.com/top250',
    #'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    #'sec-ch-ua-mobile': '?0',
    #'sec-ch-ua-platform': '"Windows"',
    #'Sec-Fetch-Dest': 'document',
    #'Sec-Fetch-Mode': 'navigate',
    #'Sec-Fetch-Site': 'cross-site',
    #'Sec-Fetch-User': '?1',
    #'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

# 在请求的时候添加请求头字段, 模拟发送请求
# headers 是指定请求头的关键字
response = requests.get('https://movie.douban.com/top250', headers=headers)
html_data = response.text
print(html_data)


"""
一般常用的请求头字段:
origin: 资源的起始位置（像root路径/目录（/）一样）
Host:客户端指定想要访问服务器的域名
Referer: 告诉服务器, 我是从哪一个链接跳转过来的
User-Agent: 浏览器的身份标识字段
cookie: 指明用户身份  --> 能不加就不加
"""

"""
为什么我请求不到数据?
    我的网络环境可能不好
    服务器可能瘫痪了
    服务器设置了一些手段, 让你不能轻易的拿到地址数据
    
    爬虫?  模拟客户端(手机, 浏览器, ....)批量请求服务器(百度,阿里, 腾讯....)数据
    
    服务器可能会针对所有的请求校验请求头字段

"""