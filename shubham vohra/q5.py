class Demo:
    def __init__(self,s=""):
        self._s=s
    def __str__(self):
        return "s:"+self.__s
    def getString(self):
        s1=input("Enter any string: ")
        self.__s=s1
    def printString(self):
        print("String converted to upper-case: "+self.__s.upper())
    def demoTesting(self):
        self.getString()
        self.printString()


d=Demo()
d.demoTesting()
