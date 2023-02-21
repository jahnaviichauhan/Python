# To find largest of three numbers

a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))

if a>b:
    if a>c:
        print("{0} is greatest".format(a))
    else:
       print("{0} is grrates".format(c))
elif  b>a:
    if b>c:
        print("{0} is greatest".format(b))
    else :
        print("{0} is greatest".format(c))