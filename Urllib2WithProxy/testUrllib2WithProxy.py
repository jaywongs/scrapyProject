#!/usr/bin/ python
#-*-coding:UTF-8-*-

import urllib2
import sys
import  re

def testArgument():
    '''测试输入参数，只需要一个参数'''
    if len(sys.argv) != 2:
        print (u'只需要一个参数就够了')
        tipUse()
        exit()
    else:
        TP = TestProxy(sys.argv[1])

def tipUse():
    '''显示提示信息'''
    print (u'只能输入一个参数，必须是可用的代理')
    print (u'usage: python testUrllib2With Proxy.py http://1.2.3.4:5')
    print (u'usage: python testUrllib2With Proxy.py https://1.2.3.4:5')

class TestProxy(object):
    '''测试proxy是否有效'''

    def __init__(self, proxy):
        self.proxy = proxy
        self.checkProxyFormat(self.proxy)
        self.url = 'http://www.zhihu.com'
        self.timeout = 5
        self.flagWord = '知乎'
        self.useProxy(self.proxy)

    def checkProxyFormat(self, proxy):
        try:
            proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
            re.search(proxyMatch,proxy).group()
        except AttributeError:
            tipUse()
            exit()
        flag = 1
        proxy = proxy.replace('//','')
        try:
            protocal = proxy.split(':')[0]
            ip       = proxy.split(':')[1]
            port     = proxy.split(':')[2]
        except IndexError:
            print (u'下标出界')
            tipUse()
            exit()
        flag = flag and len(proxy.split(':')) == 3 and len(ip.split('.')) == 4
        flag = ip.split('.')[0] in map(str,xrange(1, 256)) and flag
        flag = ip.split('.')[1] in map(str,xrange(256)) and flag
        flag = ip.split('.')[2] in map(str,xrange(256)) and flag
        flag = ip.split('.')[3] in map(str,xrange(1, 255)) and flag
        flag = protocal in [u'http',u'https'] and flag
        flag = port in map(str,xrange(1, 65535)) and flag
        '''这里是检查http代理服务器符合标准'''
        if flag:
            print (u'http代理服务器符合标准')
        else:
            tipUse()
            exit()


    def useProxy(self, proxy):
        '''利用代理访问百度，并查找关键字'''
        protocal = proxy.split('//')[0].replace(':','')
        ip = proxy.split('//')[1]
        opener = urllib2.build_opener(urllib2.ProxyHandler({protocal:ip}))
        urllib2.install_opener(opener)
        try:
            response = urllib2.urlopen(self.url, timeout=self.timeout)
        except:
            print (u'连接错误,退出程序')
            exit()
        str = response.read()
        if re.search(self.flagWord, str):
            print (u'已取得特征词,代理可用')
        else:
            print (u'该代理不可用')

if __name__ == '__main__':
    testArgument()
