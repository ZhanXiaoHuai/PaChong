import requests
#需求：用代理服务器的IP来伪装IP https://www.baidu.com/s?tn=75144485_5_dg&ch=2&ie=utf-8&wd=IP

from fake_useragent import UserAgent
ua=UserAgent()
random_user_agent=ua.getGoogle.get('useragent')

if __name__=='__main__':
    url='https://www.baidu.com/s?wd=IP'
    headers = {
        'User-Agent': random_user_agent
    }
    page_text=requests.get(url=url,headers=headers,proxies={"http":"http://47.96.252.171:80","http":"http://121.43.100.184:80"}).text#proxies代理IP和端口号 伪装IP
    with open('IP.html','w',encoding='utf-8')as fp:
        fp.write(page_text)

