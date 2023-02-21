"""
	目标地址：https://m.maoyan.com/board/4
	
	要求：
		1、请求到目标网址数据，需要在请求到的数据中看到当前页面所有的电影名字、主演、上映时间、评分等信息
		2、请列举在请求不到数据时，需要添加几个常见请求头字段（课程讲过）
		
请在下方编写代码
"""
import requests


headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'iuuid=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; ci=70%2C%E9%95%BF%E6%B2%99; _lxsdk_cuid=1803c6fc140c8-03e4923d825316-1734337f-1fa400-1803c6fc140c8; webp=true; featrues=[object Object]; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1673263907; _lxsdk_s=185964d01b7-869-bc6-e90%7C%7C2; _lxsdk=9DED7A10B17C11ECB1EFC3BD08D8135DA8FA319C52714E4EBC6C74008CD8840E; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1673264235',
    # 'Host': 'm.maoyan.com',
    # 'Pragma': 'no-cache',
    # 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'none',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

response = requests.get('https://m.maoyan.com/asgard/board/4', headers=headers)

# 指定响应体编码, 解决乱码
response.encoding = response.apparent_encoding  # 自动识别响应体编码

html_data = response.text
print(html_data)
print(response.status_code)

# 是不是被反扒?
# 没有模拟请求

"""
常见的请求头字段:
User-Agent: 浏览器的身份标识
Host: 客户端指定想要访问的服务器的域名
Cookie: 用户身份的字段 (能不加就不加)
Referer: 通过这个字段, 浏览器可以告诉服务器是从哪个链接跳转过来的(防盗链)
Origin: 资源的起始位置
"""
