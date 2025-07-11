#便捷的获取网站中动态加载的护具
#便捷实现模拟登录
#基于浏览器自动化的一个模块
#下一个浏览器的驱动程序 下载地址https://chromedriver.storage.googleapis.com/index.html   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
#驱动程序和浏览器的映射关系

#selenium可以直接获取到页面动态加载的数据 不用再去看AJAX包那么麻烦的操作了 直接获取page_source

import time
from selenium import webdriver
# edge 实例化一个浏览器对象(传入浏览器的驱动) 我放到了python解释器的路径了 就不用传了
driver = webdriver.Edge()
#让浏览器发起一个指定url对应请求
driver.get("http://www.baidu.com")

page_text=driver.page_source
print(page_text)
time.sleep(5)#暂停5秒
driver.quit()#关闭浏览器