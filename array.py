
"""This frogram will ask user to enter the array and ask the
user to search any element and print its index value"""



from array import *

arr = array('i',[])

n = int(raw_input("Enter the length of the array"))
for i in range(n):
	x = raw_input("Enter the values")
	arr.append(x)
print arr	

val = raw_input("Enter any number to search")
k=0
for e in arr:
	if e == val:
		print "Index of the Searched element is" % (k)
		break
	k=k+1	

