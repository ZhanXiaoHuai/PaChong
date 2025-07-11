#iframe标签 是HTML中用于嵌入另一个 HTML页面到当前页面中的标签
#https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
from selenium import webdriver
from selenium.webdriver.common.by import By#查找元素 通过By里的什么元素
from time import sleep
from selenium.webdriver import ActionChains#引入动作链


bro=webdriver.Edge()
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

bro.switch_to.frame('iframeResult')#如果被iframe包围直接找是找不到的 先切换到iframe中再去find
#如果定位的标签是存在于iframe标签中的 则必须通过以下方法才能定位到
div=bro.find_element(By.ID,'draggable')

action=ActionChains(bro)#传进去创建对象
action.click_and_hold(div)#点击找到的这个标签 并且按住

for i in range(0,5):
    #perform()立即执行动作链操作
    #move_by_offset(x,y)x水平方向 y竖直方向
    action.move_by_offset(17,0).perform()
    sleep(0.3)


#释放动作链
action.release()
print(div)
