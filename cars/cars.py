import sys

choice = 0

while (choice<=7):
    print("1.add new car in list")
    print("2.delete the car")
    print("3.search car on brand")
    print("4.search car based on price")
    print("5.Exit")
    
    choice=int(input("enter your choice"))

    if choice==1:
        name=input("enter car brand : ")
        num=input("enter car number : ")
        dop=input("enter date of purchase : ")
        price=input("enter price : ")
        data="\n"+name+","+num+","+dop+","+price

        with open("cardata10.csv","a+") as d:
            for i in data:
                d.write(i)
            d.close()

    elif choice==2:
        num=input("enter number to delete car data : ")
        with open("cardata10.csv","r") as r:
            data=r.readlines()
            with open("cardata10.csv","w") as w:
                for l in data:
                    if l.split(",")[1]!=num:
                        w.write(l)

    elif choice==3:
        name=input("enter car brand to search : ")
        with open("cardata10.csv","r") as r:
            data=r.readlines()
            for i in data:
                if i.split(",")[0]==name:
                    print(i)
            else:
                print("car brand search ended !!")


    elif(choice==4):
        price=input("enter car price")
        choice0=input("press 1.car less than entered price \n2.car greater than entered price [1/2] ? : ")

        if(choice0==1):
            with open("cardata10.csv","r") as r:
                data=r.readlines()
                for i in data:
                    if i.split(",")[3]<=price:
                        print(i)
        elif(choice0==2):
            with open("cardata10.csv","r") as r:
                data=r.readlines()
                for i in data:
                    if i.split(",")[3] > price:
                        print(i)

        else:
            print("invalid choice entered !!!")


    elif(choice==5):
        print("EXITING........")
        sys.exit()

    
                    
            
          
        
        
         
                        
