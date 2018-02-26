import sys

def preorder(l) :
    if len(l) <= 3 :
        if l[0] == '*' :
            return int(l[1]) * int(l[2])
        if l[0] == '/' :
            return int(l[1]) / int(l[2])
        if l[0] == '+' :
            return int(l[1]) + int(l[2])
        if l[0] == '-' :
            return int(l[1]) - int(l[2])
        if l[0] == '%' :
            return int(l[1]) % int(l[2])
    else :
        if l[0] == '*' :
            return preorder( l [ 1 : ( (len(l)+1)/2) ] )  *   preorder( l [ (len(l) + 1)/2 : ] )
        if l[0] == '/' :
            return preorder( l [ 1 : ( (len(l)+1)/2) ] )  /   preorder( l [ (len(l) + 1)/2 : ] )
        if l[0] == '+' :
            return preorder( l [ 1 : ( (len(l)+1)/2) ] )  +   preorder( l [ (len(l) + 1)/2 : ] )
        if l[0] == '-' :
            return preorder( l [ 1 : ( (len(l)+1)/2) ] )  -   preorder( l [ (len(l) + 1)/2 : ] )
        if l[0] == '%' :
            return preorder( l [ 1 : ( (len(l)+1)/2) ] )  %   preorder( l [ (len(l) + 1)/2 : ] )



i = raw_input("get me a preoder equation(seperate by space): ")

i = i.split()

for j in range(len(i)):
    print str(i[j]) + " ",
    if i[j].isdigit():
        i[j] = int(i[j])
print '= ',
print preorder(i)


