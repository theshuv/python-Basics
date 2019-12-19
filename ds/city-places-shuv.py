import sys
dic={"pune":["sinhagad_killa","shaniwar_wada","dagdushet","khadakwasla_dam","rajiv_gandhi_zoo"],"mumbai":["cst_terminal","chowpati","nariman_point","juhu"]}

print("1.Add new city and famous places within that city : ")
print("2.Display all cities & their famous places : ")
print("3.Display list of a particular city : ")
print("4.Display city of a famous place : ")
print("5.Delete a city details : ")
print("6.Modify famous places list :")
print("7.Exit.")
i=0
while(i<7):
    choice=int(input("Enter your choice : "))

    if(choice==1):
        addc=input("Enter city name to add :")
        if(dic.get(addc,-1)!=-1):
            ans=input("Entered city already exists, do you want to still add (y/n) ? : ")
            if(ans=="y"):
                addp=input("Enter famous places in city : " )
                dic[addc].append(addp)
                print("Successfully added a new city",addc)
                print(dic)
            else:
                print("Adding new city aborted .")
        else:
            addp=input("Enter famous places in city : " )
            dic[addc]=[addp]
            print("Successfully added a new city",addc)
            print(dic)

    if(choice==2):
        print(dic.keys(),"=====>>",dic.values())

    if(choice==3):
        view=input("Enter city name to view : ")
        if(dic.get(view,-1)==-1):
            print("Entered city not available in dictionary !")
        else:
            print(dic[view])

    if(choice==4):
        view=input("Enter place to find its city : ")
        lst=dic.keys()
        for k in lst:
            data=dic[k]
        if (view  in data):
            print(k) 
        else:
            ans=input("place not found in any city !, do you want to retry(y/n) ? :")
            if(ans=="y"):
                view=input("Enter place to find its city : ")
                lst=dic.keys()
                for k in lst:
                    data=dic[k]
                if (view  in data):
                    print(k)   
            else:
                print("place not found in any city !")

    if(choice==5):
        choic=input("Enter city name to delete its detail : ")
        if(dic.get(choic,-1)==-1):
            ans=input("Entered city not found, do you want to retry(y/n)? : ")
            if(ans=="y"):
                dic.pop(choic)
                print("city details successfully deleted .")
            else:
                print("deletion aborted.")
        else:
            dic.pop(choic)
            print("city details successfully deleted .")

    if(choice==6):
        choic=input("Enter city to update its values :")
        if(dic.get(choic,-1)==-1):
            ans=input("Entered city not found, do you want to retry(y/n)? : ")
            if(ans=="y"):
                bbb=input("Enter new famous places :")
                aaa={choic:[bbb]}
                dic.update(aaa)
                print(dic)
            else:
                print("Updation aborted.")
        else:
            bbb=input("Enter new famous places : ")
            aaa={choic:[bbb]}
            dic.update(aaa)
            print(dic)

    if(int(choice) in range(7,100)):
        print("Successfully terminating program.")
        sys.exit()
 
