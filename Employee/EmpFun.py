# -*- coding: utf-8 -*-


from EmpClass import *

def addRecord(empList):
    eid = int(input(' Enter Eid '))
    ename = input(' Enter Ename ')
    dept = input(' Enter Dept ')
    sal = int(input(' Enter Sal '))
    e = Emp(eid,ename,dept,sal)
    empList.append(e)
    return True

def deleteRecord(empList,eid):
    pos = 0
    for e in empList:
        if e.GetId() == eid:
            ans = input(' Do you really want to delete ' )
            if ans == 'y':
                empList.pop(pos)
                return 1
            else:
                return 2
        pos = pos+1
    else:
        return 3
    
def updateRecord(empList,eid,sal):
    pos=0
    for e in empList:
        if e.GetId() == eid:
            ans = input(' Do you really want to update ' )
            if ans == 'y':
                e.SetSal(sal)
                return 1
            else:
                return 2
        pos = pos+1
    else:
        return 3