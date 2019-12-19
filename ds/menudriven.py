import sys
citylst=["pune","mumbai","goa","solapur","latur"]

choice=0
while choice!=7:
    
    print("1.Add-city")
    print("2.Delete-city")
    print("3.Modify-city")
    print("4.Search-city")
    print("5.Add new-city at perticular index")
    print("6.Delete city from a perticular index")
    print("7.View city-name in sorted order")

    choice=input("Enter your choice :")

    if(choice=="1"):
        ct=input("Enter new city :")
        
        if(ct in citylst):
            ans=input("Entered city already exists, do you want to re-add it (y/n):")
            if(ans=='y'):
                citylst.append(ct)
                print("City added successfully .")
                print(citylst)
            else:
                    print("Not added city.")
        else:
                        citylst.append(ct)
                        print("City added successfully .")
                        print(citylst)

    if(choice=="2"):
        print(citylst)
        dele=input("Enter city name to delete: ")
        if(dele not in citylst):
            ans=input("Entered city does not exists,do you want to retry ? (y/n): ")
            if(ans=="y"):
                del1=input("Enter city name to delete: ")
                citylst.remove(del1)
                print("city removed successfully.")
                print(citylst)
            else:
                 print("city deletion aborted.")
        else:
            citylst.remove(dele)
            print("city removed successfully.")
            print(citylst)

    if (choice=="3"):
        print(citylst)
        mod=int(input("Enter old-city INDEX (0-N) to modify : "))
        new=input("Enter new-city name to modify :")
        if(mod >= len(citylst)):
            ans=input("Entered city not in list,do you want to retry(y/n) ? :")
            if(ans=="y"):
                mod=int(input("Enter old-city INDEX (0-N) to modify : "))
                new=input("Enter new-city name to modify :")
                citylst[mod]=new
                print("Successfully modified city-name")
                print(citylst)
            else:
                print("city-name modification aborted")
        else:
            citylst[mod]=new
            print("city successfully modified.")
            print(citylst)
            

    if(choice=="4"):
        ser=str(input("Enter city name to search :"))
        if(citylst.__contains__(ser)):
            print(citylst.index(ser))
        else:
            print("Entered city is not in the list.")
            print(citylst)

    if(choice=="5"):
         cname=str(input("Enter city-name to insert at perticular location :"))
         indexx=int(input("Enter index position to insert city :"))
         if(cname in citylst):
             ans=input("Entered city is already existing in list ,do you want to retry(y/n) :")
             if(ans=="y"):
                 citylst.insert(indexx,cname)
                 print("City successfully added.")
                 print(citylst)
             else:
                 print("Insertion aborted.")
         else:
             citylst.insert(indexx,cname)
             print("City successfully added.")
             print(citylst)    

    if(choice=="6"):
        cindex=int(input("Enter index no to delete a city existing at that index"))
        if(cindex > len(citylst)):
            ans=input("Entered index no is greater than length of list, do you want try (y/n) ?")
            if(ans=="y"):
                cindex=input("Enter index no to delete a city existing at that index")
                citylst.pop(cindex)
                print("city deletion at given index successfully completed")
                print(citylst)
            else:
                print("Deletion process aborted.")
        else:
            citylst.pop(cindex)
            print("city deletion at given index successfully completed")
            print(citylst)

    if(choice=="7"):
        choic=input("How do you want to sort list 1:Ascending, 2:Descending ? :")
        
        if(choic=="1"):
            citylst.sort()
            print(citylst)
        elif(choic=="2"):
            citylst.sort(reverse=True)
            print(citylst)
        else:
            print("Enter a valid choice to sort.")
            
    if(int(choice) in range(8,100)):
        print("Successfully termiating program.")
        sys.exit()
        #break
        











            
    
