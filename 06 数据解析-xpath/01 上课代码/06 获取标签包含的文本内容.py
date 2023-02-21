html_str = """
        <div> 
            <ul> 
                <li class="item-1">
                    <a href="link1.html">第一个</a>
                </li> 
                
                <li class="item-2">
                    <a href="link2.html">第二个</a>
                </li> 
                
                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li> 
                
                <li class="item-4">
                    <a href="link4.html">第四个</a>
                </li> 
                
                <li class="item-5">
                    <a href="link5.html">第五个</a> 
                </li>
            </ul>
        </div>
"""
import parsel


selector = parsel.Selector(html_str)

# 获取第四个<a>标签, 并获取其标签包含的文本

result2 = selector.xpath('//a[@href="link4.html"]/text()').getall()  # 一次提取
print(result2)



"""
    xpath语法中
    text()  作用在于获取到标签后, 可以提取标签包含的文本内容
"""