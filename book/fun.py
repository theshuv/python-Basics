

def addbook(blist):
    
    choice1=int(input("Press 1.Add at perticular position\n2.Add at end"))
    bid=input("Enter book id : ")
    name=input("Enter book name  : ")
    auth=input("Enter author name : ")
    price=input("Enter book price : ")
    pages=input("Enter number of pages : ")
    bdata=bid+","+name+","+auth+","+price+","+pages

    if(choice1==1):
        pos=int(input("Enter position to insert details : "))
        blist.insert(pos,bdata)
        print("Book details successfully added..")
    elif(choice1==2):
        blist.append(bdata)
        print("Book details successfully added..")
    else:
        print("Invalid choice entered !!!")

#------------------------------------------------------------------------------

def delbook(blist,bid):
    pos=0
    for b in blist:
        lst = b.split(",")
        if lst[0]==bid:
            blist.pop(pos)
            print("Successfully deleted data...")
            break
        pos = pos+1
        
    else:
        print("Book details not found !!! ")
        
#------------------------------------------------------------------------------

def modbook(blist,bid,price):
    pos=0
    for b in blist:
        lst = b.split(",")
        if lst[0]==bid:
            lst[3]=price
            blist[pos]=",".join(lst)
            print("Book details updated successfully...")
        pos=pos+1
    else:
        print("Book details not found !!!")

#-------------------------------------------------------------------------------

def dispauth(blist,auth):
    pos=0
    for b in blist:
        lst = b.split(",")
        if lst[2]==auth:
            print(lst)
        pos=pos+1
        
    else:
        print("searching for author ended !!!")

#-------------------------------------------------------------------------------

def sortp(blist,price):

    choice2=int(input("Press 1.Less than \n2.Greater than ? "))
    if choice2==1:
        for b in blist:
            lst=b.split(",")
            if lst[3]<= price:
                print(lst)
    elif choice2==2:
        for b in blist:
            lst=b.split(",")
            if lst[3]> price:
                print(lst)
    else:
        print("Invalid option entered !!!")

#-------------------------------------------------------------------------------

def writefile(blist):
    choice3=int(input("Press 1.over-write all data \n2.Append new data \n3.simply exit."))
    if choice3==1:
        with open("bookdata.dat","w") as wr:
            for b in wr:
                wr.write(b)

    elif choice3==2:
        with open("bookdata.dat","a") as ap:
            datalen = len(blist)
            for b in blist[datalen:]:
                ap.write(b)

    else:
        print("Exiting........\nbye--bye....")

#-------------------------------------------------------------------------------
        
        
        
        
