import requests
from lxml import etree
import os
#需求：解析下载彼岸图网图片数据 https://pic.netbian.com/4kyouxi/
#解决乱码的俩个方案：第一个直接在response的encoding直接修改 第二个局部修改img_name.encode('iso-8859-1').decode('gbk')先编码再解码 记得重新赋值回去


from fake_useragent import UserAgent
ua=UserAgent()
random_user_agent=ua.getGoogle.get('useragent')

if __name__=='__main__':
    url='https://pic.netbian.com/4kyouxi/'
    headers = {
        'User-Agent': random_user_agent
    }
    response = requests.get(url=url, headers=headers)
    #response.encoding='gbk'#修改编码 防止返回的数据中文为乱码 gbk
    page_text=response.text
    #print(page_text)
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//ul[@class="clearfix"]/li')

    #判断有无文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        img_name=li.xpath('./a/b/text()')[0]+'.jpg'
        img_src="https://pic.netbian.com"+li.xpath('./a/img/@src')[0]
        #通用处理中文乱码的解决方案
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        #print(img_name+' '+img_src)
        img_data=requests.get(url=img_src,headers=headers).content
        img_path='picLibs/'+img_name
        with open(img_path,'wb')as fp:
            fp.write(img_data)
            print(img_name,'下载成功!!!')