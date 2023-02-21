html_str = """
        <div> 
            <ul> 
                <li class="item-1">
                    <a href="link1.html">第一个</a>
                </li> 

                <li class="haha">
                    <a href="link2.html">第二个</a>
                </li> 

                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li> 

                <li class="haha">
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

# 获取所有<li>标签的属性值和<a>标签包含的文本, 只能使用一行 xpath 解决
result2 = selector.xpath('//li[contains(@class,"haha")]').getall()  # 一次提取
print(result2)
print(len(result2))

"""
    xpath语法中
        contains(@class,"haha") 表示模糊查询
        @class  根据class属性做模糊查询
        haha    模糊查询关键字, 包含次关键字的数据都会被提取
    
"""