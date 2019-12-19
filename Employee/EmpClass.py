# -*- coding: utf-8 -*-



class Emp:
    def __init__(self,eid=0,ename='',dept='',sal=0.0):
        self.eid=eid
        self.ename=ename
        self.dept=dept
        self.sal=sal
    
    def __str__(self):
        return str(self.eid)+','+self.ename+','+self.dept+','+str(self.sal)
    
    def GetId(self):
        return self.eid
    
    def GetSal(self):
        return self.sal
    
    def SetSal(self,sal):
        self.sal=sal