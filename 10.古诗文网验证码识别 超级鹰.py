import requests
from lxml import etree
from chaojiying import Chaojiying_Client#解析验证码的类
#需求：解析出所有城市名称 https://www.gushiwen.cn/

from fake_useragent import UserAgent
ua=UserAgent()
random_user_agent=ua.getGoogle.get('useragent')

if __name__=='__main__':
    url='https://www.gushiwen.cn/user/login.aspx'
    headers = {
        'User-Agent': random_user_agent
    }
    #创建一个Session对象
    session=requests.Session()

    #https://www.gushiwen.cn/RandCode.ashx 先拿到验证码的RandCode.ashx路径 再拼接出来 把验证码下载到本地
    #下载完之后 用超级鹰进行识别 识别到的字符用来进行模拟登录
    #最后将requests改为session会话 session会自动保存cookie 如果有生成的话 后续用他来发送会自带cookie上去
    page_text=requests.get(url=url,headers=headers).text#第一次还是用requests
    #print(page_text)
    tree=etree.HTML(page_text)
    code=tree.xpath('//*[@id="imgCode"]/@src')[0]#获取到验证码尾部 /RandCode.ashx
    code_url='https://www.gushiwen.cn/'+code#拼接出验证码完整路径

    #使用session来进行获取
    code_text=requests.get(url=code_url,headers=headers).content#图片用content
    with open('code.jpg','wb')as fp:
        fp.write(code_text)
        print('验证码下载成功')
    chaojiying = Chaojiying_Client('402755838', 'zhang2925385', '	971326')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result=chaojiying.PostPic(im, 1004)['pic_str']#{'err_no': 0, 'err_str': 'OK', 'pic_id': '2292011132023990001', 'pic_str': 'k09u', 'md5': '8b93ad0f3e7327c7419b675a7fe01ca0'}返回字典 取出值
    #result='asdf'
    print(result)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    url='https://www.gushiwen.cn/user/login.aspx'#正式网站
    data={
        '__VIEWSTATE': '/wEPDwUKLTU5OTg0MDIwNw8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBZGQGi0FCmPHMP+KelvQVsoBoqE2Axg==',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from':'',
        'email': '402755838@qq.com',
        'pwd': 'zhang2925385',
        'code': result,
        'denglu': '登录'
    }
    #使用session携带cookie进行发送
    src = session.post(url=url, headers=headers,data=data).text  # 图片用content
    print(src)


