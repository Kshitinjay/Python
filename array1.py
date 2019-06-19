from array import *

arr = array('i',[])
n= int(input("Enter the length"))

for i in range(n):
	x=int(input("enter the value"))
	arr.append(x)
print(arr)


val=int(input("Enter the value to search"))
k=0
for i in (arr):
	if i==val:
		print("matched")
		print(k)
		break
		k+1


print(arr.index(val))		



