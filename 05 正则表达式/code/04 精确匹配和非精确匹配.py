import pprint

text = """
回复_(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 540779999@gmail.com
Super劫Zed: 540776666@163.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397872410@qq.com，谢谢楼主
"""
import re

"""
()  代表精确匹配,先根据语法匹配字符串数据, 然后提取()内的字符
"""

result = re.findall('Super劫Zed: (.*?)@qq.com', text, re.S)
print(result)

# 如果一个正则语法规则中有多个精确匹配, 那么会返回一个列表嵌套元组的数据结构
result = re.findall('Super劫Zed: (.*?)@(.*?)\n', text, re.S)
print(result)

