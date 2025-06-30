#爬取三国演义小说所有的章节标题和章节内容https://guoxue.httpcn.com/book/sgyy/

#回头再破解

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua=UserAgent()

random_user_agent=ua.getGoogle.get('useragent')
print(random_user_agent)
if __name__=="__main__":
    #对首页的所有内容进行爬取
    headers = {
        'User-Agent': random_user_agent
    }
    url="https://guoxue.httpcn.com/book/sgyy/"
    page_text=requests.get(url=url,headers=headers).text

    #在首页中解析出章节的标题和详情页的url
    #print(page_text)
    soup=BeautifulSoup(page_text,'lxml')
    #解析章节标题和
    li_list=soup.select('.lunyu_section > ul > li')# > lunyu_section>ul > li
    #li_list = soup.find_all('li',class_='clear')  # > lunyu_section>ul > li
    fp=open('./sanguo.txt','w',encoding='utf-8')
    li_list_all=[]
    for li in li_list:
        left_span = li.find('span', class_='left')
        right_span = li.find('span', class_='right')

        li_list_all+=left_span
        li_list_all += right_span
    print(li_list_all)
    for li in li_list_all:
        title=li.string#取文本可以直接string/text/get_text()出来
        detail_url='https:'+li['href']#匹配属性值用[]
        #对详情页发起请求，解析出章节内容
        detail_page_text=requests.get(url=detail_url,headers=headers).text
        #解析出详情页中相关的章节内容
        detail_soup=BeautifulSoup(detail_page_text,'lxml')
        div_tag=detail_soup.find('div',class_='contentBox')
        #解析到了章节的内容
        #content=div_tag.text#text获取所有的文本 不用再遍历里面所有的p标签了
        content=str()
        for pag in div_tag.find_all('p'):
            content+=pag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功!!!')