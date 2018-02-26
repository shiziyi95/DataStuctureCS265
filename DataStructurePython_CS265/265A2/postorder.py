def postorder(l) :
	if len(l) == 3 :
		if l[-1] == '+' :
			return long(l[0]) + long(l[1])
		if l[-1] == '-' :
			return long(l[0]) - long(l[1])
		elif l[-1] == '*' :
			return long(l[0]) * long(l[1])
		elif l[-1] == '/' :
			return long(l[0]) / long(l[1])
		elif l[-1] == '%' :
			return long(l[0]) % long(l[1])
	else :
		if l[-1] == '+' :
			return postorder( l [ : ( (len(l)-1)/2) ] )  +   postorder( l [ ((len(l) - 1)/2) : -1] )
		if l[-1] == '-' :
			return postorder( l [ : ( (len(l)-1)/2) ] )  -   postorder( l [ ((len(l) - 1)/2) : -1] )
		if l[-1] == '*' :
			return postorder( l [ : ( (len(l)-1)/2) ] )  *   postorder( l [ ((len(l) - 1)/2) : -1] )
		if l[-1] == '/' :
			return postorder( l [ : ( (len(l)-1)/2) ] )  /   postorder( l [ ((len(l) - 1)/2) : -1] )
		if l[-1] == '%' :
			return postorder( l [ : ( (len(l)-1)/2) ] )  %   postorder( l [ ((len(l) - 1)/2) : -1] )
			
################			

i = raw_input("get me a postoder equation(seperate by space): ")

i = i.split()

for j in range(len(i)):
    print str(i[j]) + " ",
    if i[j].isdigit():
        i[j] = long(i[j])
print '= ',
print postorder(i)