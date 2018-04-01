#-*-coding:UTF-8-*-

class Fibonacci(object):
    '''返回一个斐波那契数列'''
    def __init__(self):
        self.fList = [0, 1] #设置初始列表
        self.main()

    def main(self):
        listLen = raw_input('请输入斐波那契数列长度(3-50):')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print ('得到的斐波那契数列为:\n %s ' %self.fList)

    def checkLen(self, length): #检查输入是否符合要求
        lenList = map(str, xrange(3, 51))
        if length in lenList:
            print ('输入的长度符合要求，继续运行')
        else:
            print ('只能输入3-50')
            exit()

if __name__ == '__main__':
    f = Fibonacci()