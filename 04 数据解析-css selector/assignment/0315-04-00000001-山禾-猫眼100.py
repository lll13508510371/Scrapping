"""
    使用 css 选择器将猫眼 100 全部电影信息全部提取出来。
    目标网址：https://m.maoyan.com/board/4

    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
	
	提取出来print（）打印即可
"""
import parsel
import requests

headers = {
    'Host': 'm.maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',

}

''' 进入网页之后连接url变了，要用实际的连接url，不然用上面的url连接会有乱码 '''
response = requests.get('https://m.maoyan.com/asgard/board/4', headers=headers)

html_data = response.text
print(html_data)

selector = parsel.Selector(html_data)
# print(selector)
name = selector.css('.title::text').getall()
star = selector.css('.actors::text').getall()
releasetime = selector.css('.date::text').getall()
score_part_1 = selector.css('.right>div>span::text').getall()
score_part_2 = selector.css('.right>div::text').getall()
lenth = len(name)

# print(name)
# print(star)
# print(releasetime)
# print(score_part_1+score_part_2)

for i in range(lenth):
    film = {
        'name': name[i],
        'star': star[i],
        'releasetime': releasetime[i],
        'score': score_part_1[i] + score_part_2[i]
    }

    print(film)
