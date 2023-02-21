
from selenium import webdriver  # 导入功能  # pip install selenium


# 1. 创建浏览器对象（这么说有点不严谨）应该是  创建谷歌网络驱动对象来驱动谷歌浏览器
driver = webdriver.Chrome()

# 2. 操作浏览器
driver.get('https://www.baidu.com')


input()  # 阻塞程序

# 3. 关闭浏览器
driver.quit()

"""
一旦咱们通过浏览器对象请求页面后
咱们后续的一系列操作, 和咱们平常操作浏览器页面的顺序大致是一直的
咱们的代码逻辑和操作的顺序逻辑大致也是一致的

以百度页面为例:
    打开百度页面
    在输入框中输入关键字
    回车/点击"百度一下"
"""

