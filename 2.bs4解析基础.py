import requests
from bs4 import BeautifulSoup
if __name__ =='__main__':
    #将本地的html文档中的数据加载到该对象中
    fp=open('HTML表单.html', 'r', encoding='utf-8')
    soup=BeautifulSoup(fp,'lxml')#需要解析的数据 需要用什么解析器进行解析lxml html.parser
    #print(soup)
    #print(soup.head)#返回的是第一次出现head的标签
    #print(soup.find('head')) #print(soup.head)等价于这个 返回第一次出现的

    #属性定位
    #.find('div')
    #print(soup.find('div',class_='hero_adc'))#加一个下划线 不然就成一个关键字了 或者不加用默认的attr
    #print(soup.find_all('div',class_='hero_adc'))#加一个下划线 不然就成一个关键字了 或者不加用默认的attr
    #print(soup.select(".hero_adc"))#选择器 .代表class 前端知识
    #print(soup.select(".hero_adc >ul>li")[0])# 一个>代表一个层级  [0]取第一个
    #获取标签之间的文本数据
    print(soup.select(".hero_adc >ul>li")[0].text)#text/string/get_text() text/get_text()可以获取所有的 string只能获取直系的



