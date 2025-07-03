import requests
from lxml import etree
#需求：解析出所有城市名称 https://www.aqistudy.cn/historydata/

from fake_useragent import UserAgent
ua=UserAgent()
random_user_agent=ua.getGoogle.get('useragent')

if __name__=='__main__':
    url='https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': random_user_agent
    }
    page_text = requests.get(url=url, headers=headers).text

    tree=etree.HTML(page_text)
    hotst_li_list=tree.xpath('//div[@class="bottom"/ul/li]')

#简单 直接跳过