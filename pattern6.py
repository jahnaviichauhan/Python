rows=int(input("Enter number of rows:"))
b = 5
for i in range(rows):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("\r")