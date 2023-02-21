import requests
import re  # 内置模块, 正则表达式解析模块

response = requests.get(
    'https://video-qn.ibaotu.com/19/83/83/49Z888piC4I8.mp4')
video_data = response.content

print(video_data)

with open('my.mp4', mode='wb') as f:
    f.write(video_data)
