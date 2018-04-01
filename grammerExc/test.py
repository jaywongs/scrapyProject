#-*-coding:UTF-8-*-
import os

import jayClass

GB = "-------Good bye!--------"



fo = open("foo.txt","w")
fo = open("foo.txt","r+")
fo.write("www.rockers.com!\nvery good site!\n")
str = fo.read(10)
print "读取的字符串是:",str

# 查找当前位置
position = fo.tell()
print "当前位置",position

# 把指针再次定位到文件头
position = fo.seek(4,0)
str = fo.read(10)
print "重新读取的字符串是：",str
fo.close()
os.chdir("/Users/jay/Downloads")
print os.getcwd()
print GB

# os.remove("foo.txt")

jayClass.printme("wtf???")
jayClass.printme("again")
jayClass.printme(GB)


fruits = ['banana','apple','orange']
for fruit in fruits:
    print '当前水果:',fruit
print GB

for index in range(len(fruits)):
    print '当前水果：',fruits[index]
print GB



if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    print "False"

# raw_input("wait for your input:...")
x = 'a';
y = 'b';

print x,x
print y;

s = 'ilovepython'
print s[1:5]

list = ['we','are','chiampship']
addlist = ['warriors','are','loser']
print list
print list[1:3]
print list[2:]
print list*2
print list + addlist

print max(list)
print min(list)

a = 21
b = 10
c = 12

c = a + b
print "1 - c的值为：", c

c = a * b
print "2 - c的值为：", c

c = a / b
print "3 - c的值为：", c

c = a - b
print "4 - c的值为：", c

c = a % b
print "5 - c的值为：", c

a = 2; b = 3
c = a ** b
print "6 - c的值为：", c

c = a // b
print "7 - c的值为：", c

var = 0
if (var == 0) : print "变量的值为100."
print "Python条件语句."

while (var < 10):
    print 'The var is:', var
    var  = var + 1

i = 1
while i < 10:
    i += 1
    if(i % 2 == 0):
        continue
    print i;
count  = 0;
while count < 5:
    print count,"is less than 5"
    count += 1
else:
    print count,"is not less than 5"




