import math
 
 
def isPerfectSquare(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return false
 
x= float(input('Enter value')
if (isPerfectSquare(x)):
    print("Yes")
else:
    print("No")