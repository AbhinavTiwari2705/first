print("hello")

def fact (num):
    fact=1
    if num<0:
        print("no factorial")
    else:
        for i in range(1,num+1):
            fact=fact*i
        print("factorial is ",fact)
        
num=eval(input("enter no."))
fact(num)