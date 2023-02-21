"""
1. 采集网址 https://haokan.baidu.com/tab/gaoxiao_new

2. 采集目标
	- 采集当前页面里面的数据
	- 需要需要采集以下数据:
		title 视频标题
		duration 视频时长
		fmplaycnt 播放量

    - 用正则表达式采集
"""
import requests
import re

url = 'https://haokan.baidu.com/tab/gaoxiao_new'

'''
请求头键不能包含开头带有':'的请求头,不然会报错,删掉
'''
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'BAIDUID_BFESS=9B79289047C65A05233432B75D0321A6:FG=1; BIDUPSID=9B79289047C65A05233432B75D0321A6; PSTM=1673192806; ZFY=2r0rfsY2PoyLow4ogKqD:BOrj4fMI5qunxEc9oryzgAQ:C; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1673701246; ariaDefaultTheme=undefined; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1673701420; ab_sr=1.0.1_ZTcxMTVmOWZjMzc2NWM5MDRlMGJlMDE1ZjI1MjRkZDBkZGZkYzdjZTcwNjNiOGI1NzhiZjdkZjc1YWJkOGJkYmIwMDZlNTFhMmJjNTk1ZjkzNDZiMmFiNGNmNGM5ZGVmYTM0ODIzMzM3M2Q5MjgyMjY1NDU1YTMzZjM2YmI5ZTI5MDc2OTAzNDYzNzU0YzJjNGQyMjUxMWQ1YWRhODNjZg==; reptileData=%7B%22data%22%3A%2290ae3cda65d7e3692dcf3da7bb07407f3468d3217a8170ef0d1b2a53c22d385ea77fcb9f00674bcd9931a9849c338e83a067f27c4d61d9062ad5198a8d09e368a106ab45d64018d871dd190a3e8b688d08ed67a5590edfb4ee6bba440bb4326f%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22c4e53eb5%22%7D; RT="z=1&dm=baidu.com&si=v6fv25omqgj&ss=lcvyi7k3&sl=1&tt=26du&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=7s96&hd=3wti"',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36®',
}

response = requests.get(url=url, headers=headers)

html_data = response.text
print(response.text)
'''
title 视频标题
duration 视频时长
fmplaycnt 播放量
'''
# <a target=.*? href=.*? class='ssr-videoitem-img' style=.*?><div class='ssr-img-bottom-text'>00:24</div></a>
# duration = re.findall("<a target=.*? href=.*? class='ssr-videoitem-img' style=.*?><div class='ssr-img-bottom-text'>(.*?)</div></a>", html_data, re.S)

# print(duration)
title = re.findall("<div class='ssr-videoitem-title'>(.*?)</div>", html_data, re.S)
'''
1. href .*只能取到最后一个数 因为.* 只能匹配！！！一个字符串！！！，然后 这个时候无论(.*) 还是(.*?)都只能匹配到最后那个值</a>是结尾，所以只能取到最后一个数
fmplaycnt = re.findall("<a target='_blank' href=.* class='ssr-videoitem-extinfo'>(.*?)</a>", html_data, re.S)
'''

'''
2. 两个非贪婪匹配取到六个元素，然后取（）值
'''
fmplaycnt = re.findall("<a target='_blank' href=.*? class='ssr-videoitem-extinfo'>(.*?)</a>", html_data, re.S)

'''
3.贪婪和非贪婪模式，还是贪婪取到一个字符串，然后不取开头的<a target='_blank' href=.* class='ssr-videoitem-extinfo'>，（）取到剩下的所有数据
fmplaycnt1 = re.findall("<a target='_blank' href=.* class='ssr-videoitem-extinfo'>（.*?）</a>", html_data, re.S)
'''

duration = re.findall("<div class='ssr-img-bottom-text'>(.*?)</div>", html_data, re.S)
'''
有不一样的地方用.*? (e.g.)上方的（href)，为了能够匹配到所有的数据
'''
print(title)
print(len(title))
print(duration)
print(len(duration))
print(fmplaycnt)
print(len(fmplaycnt))
# print(fmplaycnt1)
# print(len(fmplaycnt1))

'''
!!!具体问题具体看，不要纠结各种匹配得到的数据是什么样的
'''
'''
！！！这个网页有一些视频数据是静态渲染的，所以抓包抓取的ajax异步动态数据（通过fetch/XHR)没有包含这些静态视频数据，要注意这些情况
不然可能会出现有些数据没有得到的情况（这些静态视频数据）
'''