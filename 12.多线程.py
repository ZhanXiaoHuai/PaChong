import time
from multiprocessing.dummy import Pool#多线程导入头文件

def get_page(str):
    print("正在下载: ",str)
    time.sleep(2)
    print("下载成功: ", str)

start_time=time.time()

name_list={'a','b','c','d'}

pool=Pool(4)#建立四个线程池用来处理
pool.map(get_page,name_list)#多线程方法，第一个传函数 第二传参数
end_time=time.time()

print('用时：',end_time-start_time)