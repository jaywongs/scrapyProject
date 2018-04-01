#-*-coding:UTF-8-*-

class PrintTable(object):
    '''打印九九乘法表'''
    def __init__(self):
        print '开始打印九九乘法表'
        self.print99()

    def print99(self):
        for i in xrange(1, 10):
            for j in xrange(1, i+1):
                print ('%dx%d=%2s ' %(j,i,i*j)),
            print ('\n')

if __name__ == '__main__':
    pt = PrintTable()