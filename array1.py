from array import *
val=array('i',[1,2,3,4,5])
#print(val)
#print(val.buffer_info())
#for i in range(len(val)):
  #   print(val[i])
for e in val:
   print(e)
  
newarr=array(val.typecode,(b*b for b in val))   
print(newarr)
 
#taking input from user and getting index number
#arr=array('i',[])
#n=int(input("enter the length of the array\n"))
#for i in range(n):
 #   x=int(input("Enter the next element of the array"))
  #  arr.append(x)
    
#print(arr)    

#z=int(input("enter the value to be search"))
#for i in range(n):
 ##      print(arr[i],i)
 #       break
#else:
 #   print("element not found")    
  
#some functions
 
arr=array('i',[20,30,20,40,50])
 
print(arr)
print(arr.index(50))
#Sarr.reverse()
print(arr)

arr.append(60)
print(arr)
print(arr.count(20))
arr.extend([70])
print(arr)
print(arr.index(20))

#arr.pop()
#arr.pop()
#print(arr)

arr.insert(2,55)
print(arr)
arr.remove(30)
print(arr)





  