#coding:utf-8
import time
import requests
import json
import openpyxl
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions#实现规避检测
requests.packages.urllib3.disable_warnings()# 消除警告

from fake_useragent import UserAgent
ua=UserAgent()
headers = {
    'User-Agent': ua.random  # 每次请求生成随机UA
}

option=EdgeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument('--headless')
option.add_argument('--disable-gpu')

def Crawl():
    global flag_debug
    lsMakes=['MAZDA']

    for makename in lsMakes:
        pageNum = GetTotalPage(makename)
        jsn = json.loads('[]')
        for curpage in range(1, pageNum + 1):#包含最后一页
            print(f"current page: {curpage}")
            flag = PostParams(curpage, makename, jsn)
            if flag:#请求成功
                curpage += 1
            else:#请求失败
                print("error, data is None, after 5s try again")
                curpage -= 1
                time.sleep(random.uniform(4.4, 5.2))

        with open("X431/%s.json" % makename, 'w', encoding='utf-8') as f:
            json.dump(jsn, f, ensure_ascii = False)
        output2Excel(makename)

def GetTotalPage(makename):
    #点击车系抓取网页
    driver = webdriver.Edge(options=option)#规避检测+无头浏览
    driver.get("http://qcar.x431.com/qcar/#/pc/index?q=e30%3D")
    time.sleep(random.uniform(2, 3))
    vehicle_name=ConvertMakeName(makename)
    driver.find_element(By.XPATH, value=f"//p[text()='{vehicle_name}']").click()#找到对应名字进行点击
    time.sleep(random.uniform(2, 3))
    number=int(driver.find_element(by=By.XPATH, value="//li[@class='number'][last()]").text)#获取最后一个number标签->总页数
    # 等待一些时间后关闭浏览器 我是IKUN嘻嘻
    time.sleep(2.5)
    driver.quit()
    return number

def ConvertMakeName(makename):
    if 'PEUGEOT' == makename:
        return '标致'
    elif 'CITROEN' == makename:
        return '雪铁龙'
    elif 'LANDROVER' == makename:
        return '路虎'
    elif 'JAGUAR' == makename:
        return '捷豹'
    elif 'FIAT' == makename:
        return '菲亚特'
    elif 'LANCIA' == makename:
        return '蓝旗亚'
    elif 'ROMEO' == makename:
        return '阿尔法罗密欧'
    elif 'VOLVO' == makename:
        return '沃尔沃'
    elif 'LYNKCO' == makename:
        return '领克'
    elif 'USAFORD' == makename:
        return '福特'
    elif 'MAZDA' == makename:
        return '马自达'
    elif 'EV_ZEEKR' == makename:
        return '极氪'
    else:
        raise Exception('未知的makename，需要在ConvertMakeName()中添加')
        return ''

def PostParams(page, makename, jsn):
    url = "https://qcar.x431.com/proxy_qcar/serial/modelPage.action"
    proxy = {"http":None, "https":None}#解决url由http切换成https的问题
    param = {
        "swId": makename,
        "lan": "CN",
        "page": page,
        "pageSize": "20",
        "pdtType": "1"
    }

    res = requests.post(url=url, data=param,headers=headers, verify=False, proxies=proxy)
    if 200 != res.status_code:
        print("post error with page {page}, status_code {res.status_code}")
        return False
    dataJsn = res.json()#获取json内容
    data = dataJsn["data"]#仅获取data里的内容，其他状态信息不管
    jsn.append(data)
    return True

def output2Excel(makename):
    print("Outputting %s.xlsx" % makename)
    fp = open("X431/%s.json" % makename, 'r', encoding='utf-8')
    data = json.load(fp)
    wb = openpyxl.Workbook()
    ws = wb.active
    # 由于json中的元素会乱序，需要手动指定每列的元素
    lsTitle = ["rowid", "区域", "车系", "车型", "年款", "系统", "子系统", "功能", "子功能"]
    ws.append(lsTitle)
    for curpage in data:
        if curpage is None:
            continue
        for row in curpage:
            lsData = []
            lsKeys = ["ROW_ID", "region", "make", "model", "year", "system", "subSystem", "function", "subFunction"]
            for curKey in lsKeys:
                if curKey in row:
                    lsData.append(row[curKey])
                else:
                    lsData.append("")
            ws.append(lsData)
    wb.save("X431/%s.xlsx" % makename)
