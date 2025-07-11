import time

from selenium import webdriver
from selenium.webdriver.common.by import By#查找元素 通过By里的什么元素
from time import sleep#可以直接调用sllep

bro = webdriver.Edge()
bro.get('https://www.taobao.com/')

#标签定位
search_input=bro.find_element(By.ID,'q')#找到要搜索的框
#标签交互
search_input.send_keys('Iphone')#填入搜索的词

#执行一组js程序 execute_script执行js代码
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')#滚轮向下滚动一屏幕的高度
sleep(2)
#点击搜索按钮
btn=bro.find_element(By.CSS_SELECTOR,'.btn-search')
btn.click()

bro.get('https://www.baidu.com')
sleep(2)
bro.back()#浏览器进行回退
sleep(2)
bro.forward()#浏览器进行前进

sleep(5)
bro.quit()