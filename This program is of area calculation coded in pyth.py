#This program is of area calculation coded in python 
#language in this user will get two options to 
#calculate the area nd the rest of the operations 
#will be performed by the smarty python!





print "Area Calculater is Ready"
option = raw_input ("Enter C for Circle or T for Triangle:")
if option == 'C':
	radius = float(raw_input("Enter Radius"))
	area = 3.14159 ** radius
	print "Area is %s" % float(area)
elif option =='T':
	base = float(raw_input ("Enter the base of triangle"))
	height = float(raw_input("Enter the height"))
	area = 0.5 * base * height
	print "Area of triangle is %s" % float(area)
else:
	print "Invalid Choice!"
print "The Program was Exiting"

  
  
	



