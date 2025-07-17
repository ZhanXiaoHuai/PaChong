import requests

#需求：爬取道通919 431车型支持 https://www.auteltech.cn/vehicle-coverage/getData

from fake_useragent import UserAgent
ua=UserAgent()
random_user_agent=ua.getGoogle.get('useragent')

if __name__=='__main__':
    url = 'https://www.auteltech.cn/vehicle-coverage/getData?lg=cn&language=cn&product=MaxiSys%20919&carserie=%E9%A9%AC%E8%87%AA%E8%BE%BE&carName=&year=&subfunction=&pageSize=2500&pageNo=0'
    headers = {
        'User-Agent': random_user_agent
    }
    # params={
    #     'lg':'cn',
    #     'language':'cn',
    #     'product':'MaxiSys%20919',
    #     'carserie':'%E9%A9%AC%E8%87%AA%E8%BE%BE',
    #     'carName':'',
    #     'year':'',
    #     'subfunction':'',
    #     'pageSize':'2000',
    #     'pageNo':'0',
    #     'cookie':'_site_id_cookie=861; Hm_lvt_8097fb63816706f5cdb4b2ed6f03b858=1752577600; HMACCOUNT=CB9A9DC164231CF0; _ga=GA1.1.1262796831.1752577600; JSESSIONID=7F2C32EF29D673BFF543A4406A1DB5E6; JIDENTITY=03862d35-bfbf-4bcf-a8ee-664c58ced156; Hm_lpvt_8097fb63816706f5cdb4b2ed6f03b858=1752580209; _ga_M1XDRZGSVV=GS2.1.s1752577600$o1$g1$t1752580258$j7$l0$h0'
    # }
    page_text = requests.get(url=url, headers=headers,proxies={"http":"http://47.96.252.171:80"}).text  # 第一次还是用requests 获取data里的数据
    print(page_text)
    page_json=page_text['data']
    print(len(page_json))
    page_path='道通马自达数据.txt'
    with open(page_path, 'wb') as fp:
         fp.write(page_text)
         print('下载成功!!!')