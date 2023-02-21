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

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397@qq.com，谢谢楼主
-------@qq.com，谢谢楼主
"""
import re

# []  用于收集所有需要匹配的字符
# 一个字符集只能匹配到一个字符串内容
result = re.findall('[0123456789]*@qq.com', text)
print(result)

result = re.findall('[0-9]*@qq.com', text)
print(result)

# 连续的字母可以如下去写
# '-' 不代表一个字符， 而是语法表示'0到9' '到'的意思
result = re.findall('[0-9][a-zA-Z]*@qq.com', text)
print(result)

