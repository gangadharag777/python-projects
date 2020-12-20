from numpy import *
"""
arr=array([1,2,3,4,5],int)
print(arr.dtype)
print(arr)

arr=linspace(5,6,10)
print(arr)

arr=arange(2,20,2)
print(arr)

arr=ones(5,int)
print(arr)


arr=arr+5
print(arr)

arr1=array([1,4,2,1,2])
arr2=ones(5,int)
arr3=arr1+arr2
print(arr3)
print(min(arr3))
print(max(arr3))
print(sum(arr3))
print(sort(arr3))
print(concatenate([arr1,arr2]))
"""
arr1=ones(5,int)
arr2=arr1.copy() #arr.view()
arr2[2]=9
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

