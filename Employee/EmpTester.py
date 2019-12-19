# -*- coding: utf-8 -*-


import sys 
from EmpFun import *
import os

with open('empData.csv','r') as fh:
    empList=fh.readlines()
    empList=list(map(lambda x : x.rstrip("\n"),empList))
fh.close()

#empList = []
ch = 0
while ch != 6:
    print(' 1 . Add Records ')
    print(' 2 . Delete Record ')
    print(' 3 . Update Record ')
    print(' 4 . Show ')
    print(' 6 . Exit ')
    
    ch = int(input(' Enter Your Choice : '))
    if ch == 1:
        ans=addRecord(empList)
        if ans == True:
            print('Success')
    if ch == 2:
        eid = int(input(' Enter Eid To Delete '))
        ans = deleteRecord(empList,eid)
        if ans == 1:
            print('Success')
        elif ans == 2:
            print('Not Deleted')
        else:
            print('not found')
    if ch == 3:
        eid = int(input(' Enter Eid To update '))
        sal = int(input(' Enter sal To update with '))
        ans = updateRecord(empList,eid,sal)
        if ans == True:
            print('success')
    if ch == 4:
        for i in empList:
            print(i)
    if ch == 5:
        pass
    if ch == 6:
        with open('empData.csv','w') as fh:
            for i in empList:
                fh.write(str(i)+'\n')
        sys.exit()