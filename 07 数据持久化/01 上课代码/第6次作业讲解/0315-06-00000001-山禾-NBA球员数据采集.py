"""
    目标网址: https://nba.hupu.com/stats/players/pts
    
    需求:
        1、用xpath采集nba球员数据
        2、采集以下信息
            rank   # 排名
            player  # 球员
            team    # 球队
            score    # 得分
            hit_shot   # 命中-出手
            hit_rate   # 命中率
            hit_three   # 命中-三分
            three_rate   # 三分命中率
            hit_penalty   # 命中-罚球
            penalty_rate   # 罚球命中率
            session   # 场次
            playing_time   # 上场时间
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""

# 1. 找数据对应的地址
import parsel
import requests

url = 'https://nba.hupu.com/stats/players/pts'

# 2. 发送请求
response = requests.get(url=url)
html_data = response.text
print(html_data)  # 打印确认数据已经是请求到了

# 3. 解析数据
selector = parsel.Selector(html_data)
trs = selector.xpath('//tbody/tr')[1:]  #
# print(trs)
# print(type(trs))
# print(len(trs))

for tr in trs:  # for i in range(len(trs))
    rank = tr.xpath('./td[1]/text()').get()
    # print(rank)
    player = tr.xpath(f'./td[2]/a/text()').get()  # 球员
    team = tr.xpath('./td[3]/a/text()').get()  # 球队
    score = tr.xpath('./td[4]/text()').get()  # 得分
    hit_shot = tr.xpath('./td[5]/text()').get()  # 命中-出手
    hit_rate = tr.xpath('./td[6]/text()').get()  # 命中率
    hit_three = tr.xpath('./td[7]/text()').get()  # 命中-三分
    three_rate = tr.xpath('./td[8]/text()').get()  # 三分命中率
    hit_penalty = tr.xpath('./td[9]/text()').get()  # 命中-罚球
    penalty_rate = tr.xpath('./td[10]/text()').get()  # 罚球命中率
    session = tr.xpath('./td[11]/text()').get()  # 场次
    playing_time = tr.xpath('./td[12]/text()').get()  # 上场时间

    print(rank, player, team, score, hit_shot, hit_rate, hit_three, three_rate, hit_penalty,
          penalty_rate, session, playing_time, sep='\t')

# 4. 数据保存
