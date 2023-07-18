def sum_of_cubes(n):
    sum = 0
    for num in range(1, n+1):
        sum += num**3
    return sum
n = int(input("Enter a number: "))
result = sum_of_cubes(n)
print("The sum of cubes from 1 to", n, "is:", result)
