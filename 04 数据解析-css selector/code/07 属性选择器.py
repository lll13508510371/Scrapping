

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

# :: 表示属性选择器, 当你提取到标签之后, 需要对标签特定的值进行提取(标签包含的文本内容, 标签的属性)
# # text  提取标签包含的文本内容
result = selector.css('p::text').getall()
print(result)

# ::attr(href)      根据标签中包含的属性名字提取属性值
# href              a 标签的属性名字
result = selector.css('a::attr(href)').getall()
print(result)
