rows=int(input("Enter number of rows:"))
b = 0
for i in range(rows):
    for j in range(1, i + 1):
        print(b, end=" ")
        b=b+1
        
    print("\r")