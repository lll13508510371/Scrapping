"""
    使用 css 选择器将快代理中我需要的信息提取出来。
    目标网址：https://www.kuaidaili.com/free/
    
    需要解析以下数据:
        ip、
        port、
        类型
	
	提取出来print（）打印即可
"""

# 1.找请求地址
import parsel
import requests

url = f'https://www.kuaidaili.com/free/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# 2.发送请求
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
html_data = response.text
print(html_data)  # 打印请求到的数据, 查看数据是已经请求到了

# 3.数据解析
# 3.1 转换数据类型
selector = parsel.Selector(html_data)
# 3.2 解析数据-->二次提取
trs = selector.css('tbody>tr')  # 提取到所有的tr标签
print(trs)
print(len(trs))

for tr in trs:
    ip = tr.css('td:nth-child(1)::text').get()
    port = tr.css('td:nth-child(2)::text').get()
    type_ = tr.css('td:nth-child(4)::text').get()
    print(ip, port, type_)
