import sys
#print(sys.setrecursionlimit(3000))
#print(sys.getrecursionlimit())
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
result=fact(10)
print(result)