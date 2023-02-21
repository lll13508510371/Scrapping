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

import parsel
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

html_data = requests.get('https://nba.hupu.com/stats/players/pts', headers=headers).text
# print(html_data)
selector = parsel.Selector(html_data)

trs = selector.xpath('//tr')

for tr in trs[1:]:
    rank = tr.xpath('./td[1]/text()').get()
    player = tr.xpath('./td[2]/a/text()').get()
    team = tr.xpath('./td[3]/a/text()').get()
    score = tr.xpath('./td[4]/text()').get()
    hit_shot = tr.xpath('./td[5]/text()').get()
    hit_rate = tr.xpath('./td[6]/text()').get()
    hit_three = tr.xpath('./td[7]/text()').get()
    three_rate = tr.xpath('./td[8]/text()').get()
    hit_penalty = tr.xpath('./td[9]/text()').get()
    penalty_rate = tr.xpath('./td[10]/text()').get()
    session = tr.xpath('./td[11]/text()').get()
    playing_time = tr.xpath('./td[12]/text()').get()
    print(rank, player, team, score, hit_shot, hit_rate, hit_three, three_rate, hit_penalty, penalty_rate, session,
          playing_time, sep=' | ')
