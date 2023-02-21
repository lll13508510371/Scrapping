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

# 获取第三个li标签的节点
result2 = selector.xpath('//li[1]').getall()  # 一次提取
print(result2)



"""
    xpath语法中
    对于获取同级标签的第几个, 可以用 [] 精确定位到第几个
    [] 内部填标签排列的顺序, 类似于索引, 但是是从1开始的
    
    [] 用途
        1.用于精确定位
        2.用于同级标签取第几个
"""