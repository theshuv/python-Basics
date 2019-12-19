import sys
import fun as f

data=open("C:\\Users\\dbda\\Desktop\\New folder\\data.dat")
blist=data.readlines()
data.close()
datalen = len(blist)
choice=0

while(choice<8):
    
    print("1.Add new Book")
    print("2.Delete book")
    print("3.Modify price")
    print("4.Diplay by author")
    print("5.Display all")
    print("6.Sort by price")
    print("7.Exit")
    choice=int(input("Enter your choice : "))

    if(choice==1):
        f.addbook(blist)

    elif(choice==2):
        bid=input("Enter book id to delete : ")
        f.delbook(blist,bid)

    elif(choice==3):
        bid=input("Enter book id to Modify price : ")
        price=input("Enter new price : ")
        f.modbook(blist,bid,price)

    elif(choice==4):
        auth=input("Enter author name to display his books : ")
        f.dispauth(blist,auth)

    elif(choice==5):
        print(blist)
        print("**********************************************")

    elif(choice==6):
        price=input("Enter price of a book : ")
        f.sortp(blist,price)

    elif(choice==7):
        f.writefile(blist)

        sys.exit()
            
    
    
