作者：小明
版本：V0.01
日期：2025.07.17
该项目为爬取道通网站车型支持
1.https://www.auteltech.cn/vehicle-coverage/coverage2?language=cn	简称为908
2.https://qcar.x431.com/qcar/#/pc/index?q=e30%3D					简称为X431

增加了无头浏览器，如果想观察自动化效果把这两行注释
#option.add_argument('--headless')
#option.add_argument('--disable-gpu')

如需开启代理，在proxy列表里填上代理IP，格式示例：proxy = {'http':代理IP:端口号}

对于爬取的结果保存两份，一份json版本，一份xlsx版本，保存在文件夹X431/908里，名字为对应车系

908使用方法：
在Crawl函数当中->lsMakes = ['马自达','福特']	#车系名
在lsMaskes里输入对应想要查询的车系名，可一次爬取多个，每个按此格式填好
->product = 'MaxiSys 919&ADAS'	#产品名为想查找的产品名字，在网站上找到对应填上

413使用方法:
在Crawl函数当中->lsMakes=['MAZDA']	#车系名
在lsMaskes里输入对应想要查询的车系名，可一次爬取多个，每个按此格式填好，填的为车系对应的简称，在ConvertMakeName函数当中有此分支

mainProc调用对应341/908的Crawl函数即可


可扩展：
增加UI界面，先将所有车系爬取，做为可视化界面来选取对应车系进行爬取
增加多线程爬虫/多协程，提高爬取速度
