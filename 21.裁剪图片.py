from selenium import webdriver
from selenium.webdriver.common.by import By#查找元素 通过By里的什么元素
from time import sleep
from PIL import Image#进行图片裁剪

bro=webdriver.Edge()

bro.get('https://www.baidu.com')#save_screenshot就是将当前页面进行截图且保存
bro.save_screenshot('21.png')

#确定验证码图片对应的左上角和右下角的坐标（裁剪的区域 就确定）
code_img_ele=bro.find_element(By.XPATH,'//*[@id="lg"]')
location=code_img_ele.location #x,y 验证码图片左上角的坐标
size=code_img_ele.size #对应的长度和宽度
print(size)
#左上角和右下角的坐标 左上角x+宽度等于右下角x 左上角y加高度等于右下角y
rangle=(
    int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])
)
#至此图片区域就确定下来了
i=Image.open('./21.png')
code_img_name='21_code.png'
frame=i.crop(rangle)#根据指定区域进行图片裁剪
frame.save(code_img_name)

