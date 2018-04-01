#-*- coding: utf-8 -*-

import re
import urllib2

class TodayMoive(object):
	'''获取金逸影院当日影视 '''
	def __init__(self):
		self.url = 'http://www.jycinema.com/html/default/index.html'
		self.timeout = 5
		self.fileName = './todayMoive.txt'
		'''内部变量定义完毕 '''
		self.getMoiveInfo()

	def getMoiveInfo(self):
		response = urllib2.urlopen(self.url,timeout=self.timeout)
		moiveList = re.findall('film-title.*',response.read())
		with open(self.fileName,'w') as fp:
			for moive in moiveList:
				moive = self.subStr(moive)
				print (moive)
				print(moive.decode('utf8'))
				fp.write(moive + '\n')


	def subStr(self,st):
		st = st.replace('film-title">','')
		st = st.replace('</span>','')
		return st


if __name__ == '__main__':
	tm = TodayMoive()
