from selenium import webdriver
from time import sleep
#from selenium.webdriver.edge.options import Options#导入Options类 用来实现无可视化界面
from selenium.webdriver import EdgeOptions#实现规避检测的

#实现无可视化界面的操作
# Edge_options=Options()#1
# Edge_options.add_argument('--headless')#2
# Edge_options.add_argument('--disable-gpu')#3

#实现规避检测  实现无可视化界面也在此实现 都添加到EdgeOptions类统一即可
option=EdgeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument('--headless')#2
option.add_argument('--disable-gpu')#

#如何实现让selenium规避被检测到的风险
bro=webdriver.Edge(options=option)#传参进去 无头浏览器

bro.get('https://www.baidu.com')
print(bro.page_source)
sleep(2)
bro.quit()
