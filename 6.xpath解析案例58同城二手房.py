import requests
from lxml import etree
#需求：爬取58二手房中的房源信息

#25.6.30 由于增加了反反爬机制 多次访问返回的列表为带验证码的 后续回头来破解

from fake_useragent import UserAgent
ua=UserAgent()
random_user_agent=ua.getGoogle.get('useragent')

if __name__=='__main__':
    #爬取到页面源码数据
    url='https://cs.58.com/ershoufang/?q=%E9%9B%A8%E8%8A%B1%E5%85%AC%E9%A6%86'
    headers = {
        'User-Agent': random_user_agent
    }
    page_text=requests.get(url=url,headers=headers).text
    #print(page_text)
    tree=etree.HTML(page_text)
    #fp=open('58.txt','w',enconding='utf-8')
    div_list=tree.xpath('//section[@class="list"]/div')#先找出所有的div 组成一个List遍历
    #print(div_list)
    for div in div_list:
        title=div.xpath('./a/div[2]/div/div/h3/@title')[0]#./ 用./代表从当前开始 不能从/开始 不然又回到html开头了
        print(title)
        #fp.write(title+'\n')