""" Program to find factorial of a number """
num = int(input("Enter a number to find the factorial"))
def facto(num):
	result = 1
	for a in range(1,num+1):
		result = result * a
		return result
 		
facto(num)
print result