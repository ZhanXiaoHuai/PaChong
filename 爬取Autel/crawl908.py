#coding:utf-8
import os
import time
import random
import requests
import json
import openpyxl
import lxml
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
#监测状态
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import EdgeOptions#实现规避检测

option=EdgeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument('--headless')
option.add_argument('--disable-gpu')
from fake_useragent import UserAgent
ua=UserAgent()
requests.packages.urllib3.disable_warnings()# 消除警告

class CModel:
    modelName = ''
    lsYears = []
    def __init__(self):
        self.modelName = ''
        self.lsYears = list()

class CMake:
    makeName = ''
    lsModels= []
    def __init__(self):
        self.makeName = ''
        self.lsModels = list()

def Crawl():
    product = 'MaxiSys 919&ADAS'#产品名
    lsMakes = ['马自达']#车系名
    # lsMakes =['标致', '雪铁龙', '路虎', '捷豹', '菲亚特', '蓝西亚', '阿尔法·罗密欧', '阿巴斯']

    #结构：lsVehData[(makeName,lsModels[modelName,lsYears[]])]  [（车系,[车型,[年份]]）。。。]
    try:
        lsVehData = CrawlModelYears(product, lsMakes)
    except Exception as e:
        print("获取车型年份错误",e)
    # writeAllVehData(lsVehData)
    for curMake in lsVehData:
        jsnVehData = json.loads('[]')
        for curModel in curMake.lsModels:#遍历每一个车型
            for curYear in curModel.lsYears:#遍历每一个车型里具体的年份
                # step 1 get url with vehdata
                print("Getting: {0}-{1}-{2}".format(curMake.makeName,curModel.modelName,curYear))
                GetPage(product, curMake.makeName, curModel.modelName, curYear, jsnVehData)
        # step 2 write in json
        output2json(curMake.makeName, jsnVehData)
        # step 3 write in xlsx
        output2xlsx(curMake.makeName, jsnVehData)

def output2json(makename, jsnVehData):
    print("outputting %s.json" % makename)
    with open("908/%s.json" % makename, 'w', encoding='utf-8') as f:
        json.dump(jsnVehData, f, ensure_ascii=False)

def output2xlsx(makename, jsnVehData):
    print("outputting %s.xlsx" % makename)
    wb = openpyxl.Workbook()
    ws = wb.active
    # 由于json中的元素会乱序，需要手动指定每列的元素
    lsTitle = ["车型", "年款", "发动机", "底盘", "系列", "车辆类型", "系统", "子系统", "功能", "子功能", "版本", "备注"]
    ws.append(lsTitle)
    for curData in jsnVehData:
        for row in curData:
            lsData= []
            lsKeys = ["car", "carYear", "engine", "chassis", "bMWSeries", "gMCarType", "system", "systemSub", "function", "functionSub", "version"]
            for curkey in lsKeys:
                if curkey in row:
                    lsData.append(row[curkey])
                else:
                    lsData.append("")
            # 单独处理备注
            if "showStrings" in row:
                lsShowString = row["showStrings"]
                if lsShowString is None or 0 == len(lsShowString):
                    lsData.append("")
                else:
                    strBuf = ""
                    for curStr in lsShowString:
                        strBuf += curStr
                        strBuf += "|"
                    lsData.append(strBuf)
            ws.append(lsData)
    wb.save("908/%s.xlsx" % makename)

#监测Loading状态 CSS样式style=display: none;时退出
def Monitoring_loading_style(driver):
    # 当出现css样式时结束轮询->加载完毕
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4][@style='display: none;']")))
    except Exception as e:
        print("检查时发生错误",e)


def GetPage(product, makename, modelname, year, jsnVehData):
    url = "https://www.auteltech.cn/vehicle-coverage/getData?"
    proxy = {"http":None, "https":None}#解决url由http切换成https的问题
    header = {
        'User-Agent': ua.random,  # 每次请求生成随机UA
        "X-Requested-With": "XMLHttpRequest"
    }
    param = {"pageNo": 0,
             "product": product,
             "carserie": makename,
             "carName": modelname,
             "year": year,
             "subfunction": '',
             "language": 'cn',
             "pageSize": 2000}
    # 部分车系的年款必须为空，否则查不到
    MakesWithEmptyYear = {'标致', '雪铁龙'}
    if makename in MakesWithEmptyYear:
        param['year'] = ''
    while(1):
        res = requests.get(url=url, params=param,headers=header, verify=False, proxies=proxy)
        if 200 == res.status_code:
            dataJsn = json.loads(res.text)  # 格式化成json格式
            data = dataJsn["data"]  # 仅获取data里的内容，其他状态信息不管
            jsnVehData.append(data)
            break
        else:
            print("post error with {makename} - {modelname} - {year}, status_code {res.status_code}")
            time.sleep(random.uniform(4.3, 5.7))


def CrawlModelYears(product, lsMakes):#存某产品某车的车型和对应年份
    driver = webdriver.Edge(options=option)#规避检测+无头浏览
    driver.get("https://www.auteltech.cn/vehicle-coverage/coverage2?language=cn")

    # 找到机型输入框 - 父节点 id动态更改
    nodeProductInput = driver.find_element(by=By.XPATH, value="//p[@class='label' and text()='机型']/..")
    nodeProductInput.find_element(by=By.XPATH, value="./div/div/i").click()
    # 点击具体产品
    nodeArrowDown = nodeProductInput.find_element(by=By.XPATH, value=f"./div/div[2]/ul/li[text()='{product}']")
    nodeArrowDown.click()
    Monitoring_loading_style(driver)

    lsMakeData= []
    for curMake in lsMakes:#遍历需要爬取的车系
        mk = CMake()
        mk.makeName = curMake
        # 找到车系输入框 - 父节点 id动态更改
        nodeVehicleInput = driver.find_element(by=By.XPATH, value="//p[@class='label' and text()='车系']/..")
        nodeVehicleInput.find_element(by=By.XPATH, value="./div/div/i").click()
        # 点击具体车系
        nodeArrowDown = nodeVehicleInput.find_element(by=By.XPATH, value=f"./div/div[2]/ul/li[text()='{curMake}']")
        nodeArrowDown.click()
        time.sleep(random.uniform(0.5, 0.6))  # 点完给一个反应时间

        #找到搜索框并点击
        # nodeSelect = driver.find_element(by=By.XPATH,value="//*[@id='app']/div/div/div[1]/div/div")
        # nodeSelect.click()

        #点击车型选择按钮 保存所有车型
        nodeModelInput = driver.find_element(by=By.XPATH, value="//p[@class='label' and text()='车型']/..")
        nodeModelInput.find_element(by=By.XPATH, value="./div/div/i").click()
        nodesModelLis = nodeModelInput.find_elements(by=By.XPATH, value="./div/div[2]/ul/li")#保存所有的车型
        Monitoring_loading_style(driver)#填完车型监测状态
        for curModel in nodesModelLis:
            if ('ALL'!= curModel.text):
                md = CModel()
                md.modelName = curModel.text
                # runtime debug 点击任意车型后下拉菜单的车型列表就消失了，需要提前缓存所有车型名
                mk.lsModels.append(md)

        # 点击车型 才能加载出年份 不能直接remove readonly->sendkeys
        for curModel in mk.lsModels:
            time.sleep(random.uniform(0.6, 1))
            WebDriverWait(nodeModelInput, 15).until(#容错防止未加载完毕
                EC.element_to_be_clickable((By.XPATH, f"./div/div[2]/ul/li[text()='{curModel.modelName.strip()}']"))
            )
            nodeModelInput.find_element(by=By.XPATH, value=f"./div/div[2]/ul/li[text()='{curModel.modelName.strip()}']").click()
            # 填完车型后监测css
            Monitoring_loading_style(driver)
            nodeYearInput = driver.find_element(by=By.XPATH, value="//p[@class='label' and text()='年款']/..")
            nodeYearInput.find_element(by=By.XPATH,value="./div/div/i").click()
            nodesYearLis = nodeYearInput.find_elements(by=By.XPATH, value="./div/div[2]/ul/li")
            for curYear in nodesYearLis:
                print("create menu: {0}-{1}-{2}".format(curMake,curModel.modelName,curYear.text))
                curModel.lsYears.append(curYear.text)
            # 每次选择下一个车型都需要点击下拉框
            nodeModelInput.find_element(by=By.XPATH, value="./div/div/i").click()
        lsMakeData.append(mk)
    # 等待一些时间后关闭浏览器 我是IKUN嘻嘻
    time.sleep(2.5)
    driver.quit()
    return lsMakeData

#将所有数据写到xml文件中
def writeAllVehData(lsMakeData):
    with open('908/VehData.xml', 'w', encoding='utf-8') as fp:
        for curMake in lsMakeData:
            fp.write(curMake.makeName + "\n")
            for curModel in curMake.lsModels:
                fp.write("\t" + curModel.modelName + "\n")
                for curYear in curModel.lsYears:
                    fp.write("\t\t" + curYear + "\n")
            fp.write("\n")

