def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        temp=a+b
        if temp<=100:
            a=b
            b=temp
            print(temp)
        else:
            break
            
n=int(input("enter the range of fib"))
if n<0:
    print("negative number")
else:
    fib(n)
        