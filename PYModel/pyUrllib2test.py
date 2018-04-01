#-*-coding:UTF-8-*-

import urllib2
import os
import time
import platform

def clear():
    '''该函数用于清屏'''
    print (u'内容较多，显示三秒钟后翻页')
    time.sleep(3)
    OS = platform.system()
    if (OS == u'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def linkBaidu():
    url = 'http://www.google.com'
    try:
        response = urllib2.urlopen(url, timeout=3)
    except urllib2.URLError:
        print(u'网络地址错误')
        exit()
    with open('./google.txt', 'w') as fp:
        fp.write(response.read())
    print(u"获取URL信息, response.geturl() \n: %s" %response.geturl())
    print(u"获取返回代码, response.getcode() \n: %s" %response.getcode())
    print(u"获取返回信息, response.info() \n: %s" %response.info())
    print(u"获取的内容存入当前目录的google.txt中")

if __name__ == "__main__":
    linkBaidu()