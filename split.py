def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[]
li= list(map(int, input ().split ()))
x = removeDuplicate(li)

for i in x:
    print(i,end=" ")
    
 #another code
   
    
L=input().split()
new_list=[]
for d in L:
  if d not in new_list:
     new_list.append(d)
print(*new_list,end="")