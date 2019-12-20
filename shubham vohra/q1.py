
dic={}

def func(n):
    for i in range(1,n+1):
        dic[i]=(i*i)
    print(dic)



n=int(input("ENTER THE NUMBER : "))

func(n)
