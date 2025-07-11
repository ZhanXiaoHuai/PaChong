from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By#查找元素 通过By里的什么元素

bro=webdriver.Edge()

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')
a_tag=bro.find_element(By.ID,'switcher_plogin')
a_tag.click()

userName_tag=bro.find_element(By.ID,'u')
password_tag=bro.find_element(By.ID,'p')

userName_tag.send_keys('402755838')
password_tag.send_keys('zhang82925385')

submit_tag=bro.find_element(By.ID,'login_button')
submit_tag.click()

sleep(10)


bro.quit()
