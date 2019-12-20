import sys
min=2000
max=3200

lst=[]

while min<=max :
    if min%7==0:
        if min%5!=0:
            b = str(min)+"\n"
            lst.append(b)
    min=min+1

    #print(lst)
            
with open ("csvfile.csv","w") as file:
    for i in lst:
        file.write(i)
    file.close()
