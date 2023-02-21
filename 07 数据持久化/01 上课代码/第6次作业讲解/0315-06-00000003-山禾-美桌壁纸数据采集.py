"""
    目标网址: http://www.win4000.com/zt/dongman.html
    
    需求:
        "动漫桌面壁纸" 文字下面有很多动漫图集
        1、用xpath采集数据
        2、采集以下信息
            采集动漫图集的标题
            采集动漫图集中图片对应的url地址
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""
# 1. 找数据对应的地址
import parsel
import requests

url = 'http://www.win4000.com/zt/dongman.html'
headers = {
    'Cookie': 't=6cb8b7a33b2a435da96c3d17002c9783; r=1356',
    'Host': 'www.win4000.com',
    'Referer': 'http://www.win4000.com/zt/dongman.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

# 2. 发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
print(html_data)  # 打印确认数据已经是请求到了

# 3. 解析数据
selector = parsel.Selector(html_data)
lis = selector.xpath('//div[@class="list_cont Left_list_cont  Left_list_cont1"]//ul/li')


for li in lis:
    title = li.xpath('.//p/text()').get()
    img_url = li.xpath('.//img/@data-src').get()
    print(img_url)
