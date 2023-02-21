import re

str1 = "540775360@qq.com"
str2 = "python = 9999， c = 7890， c++ = 12345"
str3 = "python = 997"

# re.compile()   将正则表达式编译成一个对象
pattern = re.compile('\d+')
print(pattern)
print(type(pattern))

result = re.findall(pattern, str1)
print(result)

result = re.findall(pattern, str2)
print(result)

result = re.findall(pattern, str3)
print(result)



