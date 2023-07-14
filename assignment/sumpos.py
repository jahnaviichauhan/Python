def sum_positive_values(*args):
    sum_positive = 0

    for num in args:
        if num > 0:
            sum_positive += num

    return sum_positive
result1 = sum_positive_values(2, 4, -6, 8, -3, 10)
result2 = sum_positive_values(0, -1, -2, -3)
result3 = sum_positive_values(5, 10, 15)
print("Sum of positive values:", result1)
print("Sum of positive values:", result2)
print("Sum of positive values:", result3)
