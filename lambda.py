"""
f=lambda a:a*a

a=f(5)
print(a)

#         filter
num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda a:a%2==0,num))
print(even)
"""

#  map function

num=[1,2,3,4,5,6,7,8,9]
num1=list(map(lambda a:a*a,num))
print(num1)


#reduce function

from functools import reduce
sum=reduce(lambda a,b:a+b,num)
print(sum)