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


# 1.转化类型, 能够把缺失的主要的html标签补充完整
selector = parsel.Selector(html_str)
print(selector)

# 从根节点开始, 获取所有的<a>标签
result = selector.xpath('/html/body/div/ul/li/a').getall()
print(result)

"""
    xpath语法中
    /   表示从根节点开始提取<用得少>, 还用于取下一级标签
    html标签是根节点
"""