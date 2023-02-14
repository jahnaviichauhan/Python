rows=int(input("Enter number of rows:"))
b = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(b, end=" ")

    print("\r")