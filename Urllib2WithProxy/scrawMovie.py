#-*-coding:UTF-8-*-

import re
import urllib2
import scrapy


class TodayMovie(object):
    '''爬取通知'''
    def __init__(self):
        self.url = 'http://software.nju.edu.cn/index.php?option=com_content&view=category&id=66&Itemid=12'
        self.timeout = 5
        self.fileName = './ImportantNoi.txt'
        self.getNotificationInfo()

    def getNotificationInfo(self):
        try:
            response = urllib2.urlopen(self.url, timeout=self.timeout)
            NotiList = re.findall(r'catid=66:gfy&amp;Itemid=12">[\s\S]*?</a>', response.read())
        except urllib2.URLError:
            print (u'网络地址错误')
            exit()
        with open(self.fileName,'w') as fp:
            # fp.write(response.read())
            for noti in NotiList:
                noti = self.subStr(noti)
                # print (noti.decode('utf8'))
                fp.write(noti + '\n')

    def subStr(self,str):
        str = str.replace('catid=66:gfy&amp;Itemid=12">', '')
        str = str.replace('</a>', '')
        return str
if __name__ == '__main__':
    tm = TodayMovie()