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
	<p class="top" id="contend">标签选择器、类选择器、ID选择器</p>
	<a href="https://www.baidu.com">百度一下</a>
	<span> 我是一个span标签</span>
</body>
</html>
"""
import parsel

selector = parsel.Selector(html)

# '#'  使用 id 选择器提取数据
# 只要标签具有 id 属性, 那么所有具有相同id属性的标签都会被提取到
# id 在html中一般是唯一的, 但有一些二流程序员会搞多个相同id的不同数据
# contend 代表id属性的属性值
result = selector.css('#contend').getall()
print(result)
