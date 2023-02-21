# 简化的html标签, 模拟一下数据是请求到的html数据

html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>标签选择器</title>
</head>
<style>
	p{
		color: #f00;
		font-size: 16px;
	}
</style>
<body>
	<p>css标签选择器的介绍</p>
	<p>标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel  # 第三方模块 pip install parsel  提供了三种数据解析方法(css, xpath, re)


# 1.将html字符串对象转化成可解析的对象
# parsel.selector() --> 过时了
selector = parsel.Selector(html)
print(selector)

# 2.根据转化对象调用css提取方法
"""
所有通过css选择则器解析出来的数据都是一个对象(Selector)
get() 从 Selector 对象中提取第一个数据, 直接返回字符串数据给我们
getall() 从 Selector 对象中提取提取所有数据, 返回一个列表
"""
# 标签选择器: 根据标签名提取到标签对象
result = selector.css('p').get()
print(result)

result = selector.css('p').getall()
print(result)
