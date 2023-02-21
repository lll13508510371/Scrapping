import re  # 内置

string = 'PythonahsdgjasghPythonasdjajsk'

# Python  需要匹配的字符串;   string 需要在哪个字符串中匹配内容
# re.match 匹配字符串头部的数据内容, 只能在字符串头部匹配数据
# 如果找到了就返回 re.Match 对象, 可以使用 对象.group()
result = re.match('Python', string)
print(result)
print(type(result))
print(result.group())  # -->字符串（对象）--> 习惯说字符串
print(type(result.group()))
