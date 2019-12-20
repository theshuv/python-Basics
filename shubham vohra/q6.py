


def func():
    for num in range(100,501):
        if num%2!=0:
            with open("textfile.txt","a+") as t:
                num=str(num)
                
                
                t.write(str(num)+",")
            
            
        


func()        

