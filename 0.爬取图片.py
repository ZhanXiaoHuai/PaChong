import requests

if __name__=='__main__':
    url='https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00762-1578.jpg'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
    }

    response=requests.get(url=url).content
    print(response)
    with open('./baidupic.jpg','wb')as fp:
        fp.write(response)