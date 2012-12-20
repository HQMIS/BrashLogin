#-*-coding:utf-8-*-

# script: BrashLogin.py
# author: huangqimin@baidu.com

# note: 
# 1、This Python Script use Library requests:
#    see http://docs.python-requests.org/en/v1.0.0/
# 2、执行byhh.login()会发生失败的情况，导致程序Crash：
#    通过使用try...except...来容错 

import requests
import random
import time

class BYHH:
    def __init__(self, username, password):
        self.id = username
        self.pw = password
 
    def login(self):
        data = {'id': self.id, 'pw': self.pw}
        r = requests.post('http://bbs.whnet.edu.cn/cgi-bin/bbslogin', data=data)       
        print r.text
 
if __name__ == '__main__':
    username = raw_input("UserName:")
    password = raw_input("PassWord:")
    count = int(raw_input("Count:"))

    sleeptime = 15

    byhh = BYHH(username, password)
    for i in range(0, count):
        try:
            byhh.login()
        except:
            print ">>> Failed Login"
        print ">>>" + username + ' has login %d times' %(i+1)
        # BYHH会检测，是否为机器登录
        # 看到的是如果sleeptime时间为一个数，则被判为机器登录
        # 所以这里生成随机数来处理
        sleeptime = 15 + random.randint(0, 15)
        time.sleep(sleeptime)
         
