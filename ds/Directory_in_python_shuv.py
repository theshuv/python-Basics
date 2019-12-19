
import sys
cources={"DBDA":"53","DAC":"220","DITIS":"41","DSDEM":"45"}
print("*****  COURCE MANAGEMENT USING DICTIONARY  *****")
print("1.Add cource")
print("2.Delete cource")
print("3.Modify number")
print("4.Find cource details")
print("5.View students in cource")
print("6.Exit")

a=0
while(a!=6):
    choice=input("Enter your choice : ")
    if(choice=="1"):
        cn=input("Enter cource : ")
        num=int(input("Enter number of students in above cource : "))
        if(cources.get(cn,-1)!=-1):
            ans=input("Entered Cource-name(key) already exists, do you want to still overwrite (y/n) ? :")
            if(ans=="y"):
                cources[cn]=num
                print("Cource details successfully overwritten.")
            else:
                ("Cource details NOT overwritten.")
        else:
            cources[cn]=num
            print(cources)
            print("Cource details successfully Added.")

    if(choice=="2"):
        cn=input("Enter cource name to Delete : ")
        if(cources.get(cn,-1)==-1):
            ans=input("Entered cource details not found !, do you want to retry (y/n) : ")
            if(ans=="y"):
                cn=input("Enter cource name to Delete : ")
                del(cources[cn])
                print(cources)
                print("Cource details successfully deleted .") 
            else:
                print("Deletion aborted.")
        else:
            del(cources[cn])
            print(cources)
            print("Cource details successfully deleted .")

    if(choice=="3"):
        cn=input("Enter cource name to modify : ")
        if(cources.get(cn,-1)==-1):
            ans=input("Entered cource details not found !, do you want to retry (y/n) : ")
            if(ans=="y"):
                cn=input("Enter cource name to modify : ")
                num=int(input("Enter the number of students in above cource : "))
                cources[cn]=num
                print(cources)
                print("cource details successfully updated .")
            else:
                print("Details modification aborted .")
        else:
            num=int(input("Enter the number of students in above cource : "))
            cources[cn]=num
            print(cources)
            print("cource details successfully updated .")
            
    if(choice=="4"):
        cn=input("Enter the cource name to view Details : ")
        if(cources.get(cn,-1)==-1):
            ans=input("Entered cource details not found !, do you want to retry (y/n) : ")
            if(ans=="y"):
                cn=input("Enter the cource name to view Details : ")
                print("Details are as follows ->")
                print(cources[cn],"students in",cn,"cource .")
            else:
                print("Viewing details aborted .")
        else:
            print("Details are as follows ->")
            print(cources[cn],"students in",cn,"cource .")

    if(choice=="5"):
        for cn in cources.keys():
             if (int(cources[cn])<60):
                 print(cources[cn])
             else:
                 print("NO COURCE DETAILS FOUND ")

    if(int(choice) in range(6,100)):
        print("Successfully terminating program.")
        sys.exit()
        #break
