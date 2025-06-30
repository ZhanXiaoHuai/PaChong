import requests
from lxml import etree
import os
#需求：解析下载彼岸图网图片数据 https://pic.netbian.com/4kyouxi/
#解决乱码的俩个方案：第一个直接在response的encoding直接修改 第二个局部修改img_name.encode('iso-8859-1').decode('gbk')先编码再解码 记得重新赋值回去

#暂时不知道 怎么获取到Content-type已经是img类型的怎么获取，浏览器请求这个网址默认就会进行下载文件 而我们获取这个.content也没用 发起链接无法下载

from fake_useragent import UserAgent
ua=UserAgent()
random_user_agent=ua.getGoogle.get('useragent')

if __name__=='__main__':
    url='https://pic.netbian.com/4kyouxi/'
    headers = {
        'priority':'u=0,i',
        'sec-ch-ua':'"Not)A;Brand";v="8","Chromium";v="138","MicrosoftEdge";v="138"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'none',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1',
        'Cookie':'zkhanecookieclassrecord=%2C54%2C55%2C; PHPSESSID=u2o27ctv5afmhlu2r1gcvo5k33; zkhanmlusername=%B1%A7%D7%DF%D0%A1%E6%C3; zkhanmluserid=8020653; zkhanmlgroupid=1; zkhanmlrnd=Z6BhGG4PnPPzV9pFy7sw; zkhanmlauth=1e01e158528ebcc810517f29fb7bbdfe'
    }
    #还要加上cookie值
    response = requests.get(url=url, headers=headers)
    response.encoding='gbk'#修改编码 防止返回的数据中文为乱码 gbk
    page_text=response.text
    #print(page_text)
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//ul[@class="clearfix"]/li')

    #判断有无文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        Token_name=li.xpath('./a/b/text()')[0]+'.jpg'
        #"https://pic.netbian.com"
        Token_src=li.xpath('./a/@href')[0]
        #获取图片对应的id
        Token_src=Token_src.split('/')[2].split('.')[0]
        #获取ID对应的实时Token值
        Token_src="https://pic.netbian.com/e/extend/downpic.php?id="+Token_src
        #print(Token_name + ' ' + Token_src)

        Token_data=requests.get(url=Token_src,headers=headers).text
        #print(Token_data)
        keyword='token='
        token_index=Token_data.find(keyword)
        result_token=Token_data[token_index+len(keyword):]
        #print(result_token)#token值
        url_last='https://pic.netbian.com/e/extend/downpic.php?token='+result_token
        response_img=requests.get(url=url_last,headers=headers).content
        #print(response_img)
        #print(text_token)
        img_path='picLibs/'+Token_name
        with open(img_path,'wb')as fp:
            fp.write(response_img)
            print(Token_name,'下载成功!!!')