import arcpy
import numpy as np
r=int(input("").strip())
c=int(input("").strip())
a=[]
for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(int(input().strip()))
    a.append(temp)
arr=np.asarray(a)
arr.ravel().argsort().argsort().reshape(arr.shape)

print(arr)