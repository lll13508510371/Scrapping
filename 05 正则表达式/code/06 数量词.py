import pprint

text = """
回复_(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4

540775360123456@qq.com
540775360987654@qq.com
540775360956321@qq.com

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397@qq.com，谢谢楼主
"""
import re


result = re.findall('\d*@qq.com', text)
print(result)

# {数字}  只能匹配指定数字的次数
# {最小次数,}  匹配大于等于最小次数的字符
# {,最大次数}  匹配小于等于最大次数的字符
# {最小次数,最大次数}  匹配大于等于最小次数小于等于最大次数的字符
result = re.findall('\d*@qq.com', text)
print(result)

result = re.findall('\d{1,4}@qq.com', text)
print(result)
