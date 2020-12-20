"""def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

a,b=add_sub(5,8)
print(a,b)

def update(lst):
    print(id(lst))
    
    lst[2]=25
    print(lst)
    
list=[20,30,40,50] 
print(id(list))
update(list)
print(list)
print(id(list))   

# TYPES OF ARDUMENTS IN FUNCTIONS
#           default
#           keyword
#           position
#           variable length arguments




#            posittion

def person(name,age):
    print(name)
    print(age)
    
person('ganga',22)


#            default
def person(name,age=18):
    print(name)
    print(age)
    
person('gan')


#               keyword
def person(name,age):
    print(name)
    print(age)
    
person(age=22,name='gange')



#           variable length
def add(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
add(1,2,3,4)    

def person(name,**data):
    print("name=",name)
    for i,j in data.items():
        print(i,"=",j)
    
person(name='gana',age=22,city='mysore')   


#    passing list to a function

list=[1,2,3,4,5]
print(list)

def count(lst):
    evn=0
    odd=0
    for i in range(5):
        if list[i]%2==0:
            evn+=1
        else:
            odd+=1
    return evn,odd 


evn,odd=count(list)
print("even={} and odd={}".format(evn,odd))     
"""
str=[]
for i in range(5):
    str.append(input("enter next name\n"))
    
def count(lst):
    c=0
    for i in str:
        c=len(i)
        if c>=5:
            print(i)
count(str)            
            

    
    
    
    
    