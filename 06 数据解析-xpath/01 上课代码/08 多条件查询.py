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

# 获取所有<li>标签的属性值和<a>标签包含的文本, 只能使用一行 xpath 解决
result2 = selector.xpath('//li/@class|//a/text()').getall()  # 一次提取
print(result2)

"""
    xpath语法中
    |   表示多条件查询, 左右两边分别链接两个条件, 只要标签满足其中一个条件, 就会被匹配到
    用的不多
"""