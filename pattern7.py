row=int(input("Enter number of rows:"))
for i in range(row):
    for j in range(1, row - i):
        print(" ", end="")
    for k in range(1, i + 2):
        print(k, end='')
    print()