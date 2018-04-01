class classTest:
    def prt(self):
        print(self)
        print(self.__class__)

t = classTest()
t.prt()