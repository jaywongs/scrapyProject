#-*-coding:UTF-8-*-

import random

class SelectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = raw_input('输入测试的次数: ')
            try:
                num = int(numStr)
            except ValueError:
                print ('要求输入一个整数: ')
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sumA = float(0)
        for i in xrange(num):
            j = random.randint(1, 10)
            ball[j-1] += 1

        for i in xrange(1, 11):
            print (u'选中%d号球的概率为：%f' %(i, ball[i-1]*1.0/num))
            sumA += ball[i-1]*1.0/num
        print ('总概率为：%f' %sumA)

if __name__ == '__main__':
    SB = SelectBall()
