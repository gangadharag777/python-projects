from statistics import mean
from scipy import stats
list=[20,33,44,66,89,10,40,50,28,49,55,41,21,11,13,14,15,16,78,79,70]
list.sort()
"""
trim=int(0.1*len(list))
print(list)
print(trim)
list=list[trim:]
list=list[:len(list)-trim]
print(list)
print(mean(list))
"""
m=stats.trim_mean(list,0.1)
print(m)