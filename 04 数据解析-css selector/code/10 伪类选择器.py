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
	<p class="top" id="contend">css标签选择器的介绍</p>
	<p class="top">标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel

selector = parsel.Selector(html)

# : 表示伪类选择器: 取所有符合条件的第几个标签
result = selector.css('p:last-of-type').getall()
print(result)

result = selector.css('p:nth-child(2)')
print(result)

result = selector.css('p:nth-last-child(1)')
print(result)
