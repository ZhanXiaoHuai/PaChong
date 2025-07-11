from flask import Flask
import time

app=Flask(__name__)
#搭建一个服务器 三个页面 /bobo /jay /tom

@app.route('/bobo')#斜杠开头
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'

if __name__=='__main__':
    app.run(threaded=True)