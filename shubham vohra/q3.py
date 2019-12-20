lst=[]
i=0
def func(a):
    a=a.strip(",")
    a=a.split(",")
    for i in a:
        lst.append(i)
    
    

a=input("enter words seperated by comma : ")
func(a)
lst.sort()
print(lst)

