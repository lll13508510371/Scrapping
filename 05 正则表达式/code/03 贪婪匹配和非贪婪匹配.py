import pprint

text = """
回复_(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 540775360@qq.com
Super劫Zed: 540775360@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。
Super劫Zed: 540775360@qq.com
Super劫Zed: 540775360@qq.com
Super劫Zed: 540775360@qq.com

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397872410@qq.com，谢谢楼主
"""
import re

"""
正则表达式会默认使用贪婪模式
贪婪模式: 在满足正则表达式的规则前提下, 尽可能多的匹配数据
        一旦在文本中有两个地方的数据符合规则, 那么会把这两个地方及其中间的字符串匹配到以后一起返回

?   匹配1次或者0次, 在正则语法中一旦加了 ? 表示使用非贪婪模式匹配
非贪婪模式: 匹配一次返回一次 --> 要记得在？后面添加约束，不添加约束会因为
                            非贪婪模式尽可能少的匹配数据匹配0次而不返回相应的数据

.*?
"""
result = re.findall('Super劫Zed: .*@qq.com', text, re.S)
pprint.pprint(result)
print(result)
print(len(result))

result = re.findall('Super劫Zed: .*?@qq.com', text, re.S)
print(result)
print(len(result))

