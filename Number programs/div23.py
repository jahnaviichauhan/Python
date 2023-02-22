#Checking if a number is divisible by 2 and 3 both

#Inputting number
n=int(input("Enter number"))

if n%2==0 and n%3==0:
    print("{0} is divisible by 2 and 3 both".format(n))
else:
    print("{0} is not divisible by 2 and 3 both".format(n))
    