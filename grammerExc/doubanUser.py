# -*-coding:utf-8-*-

import requests
from lxml import html

cookie = {}

raw_cookies = 'e46f388057efee24.1507419030.3.1522062403.1522051077.'

for line in raw_cookies.split(';'):
    key, value = line.split('=', 1)
    cookie[key] = value

page = requests.get('https://www.douban.com/people/zhangjiawei/', cookies=cookie)

tree = html.fromstring(page.text)

intro_raw = tree.xpatch('//span[@id = "intro_display"]/text()')

for i in intro_raw:
    intro = i.encode('utf-8')

print intro

