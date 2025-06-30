import requests
import re
import os
if __name__ =='__main__':
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./pictures'):
        os.mkdir('./pictures')

    url='https://sucai.mixinnet.cn/subject/114.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
    }
    response=str()
    for i in range(1,8):#爬取1-7页
        #使用通用爬虫对url对应的一整张页面进行爬取
        params = {
            'page':str(i)
        }
        response+=requests.get(url,headers=headers,params=params).text
        #print(List_response)

    #正则表达式匹配规则 .*?匹配所有字符 ()里的就是匹配组里的数据
    ex=r'<div class="gallery-item mixinnet".*?<img src="(.*?)" alt.*?</div>'
    img_src_list=re.findall(ex,response,re.S)#re.S单行爬取 匹配上换行符Single M多行爬取 Multi
    print(img_src_list)

    for src in img_src_list:
        #请求到图片的二进制数据
        img_data=requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name=src.split('/')[4].split('?')[0]
        #图片存储的路径
        img_path='./pictures/'+img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功')
