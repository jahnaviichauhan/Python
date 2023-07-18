def sum_of_squares(numbers):
    squares = map(lambda x: x**2, numbers)
    sum_of_squares = sum(squares)
    return sum_of_squares

# Take input from the user
user_input = input("Enter a list of numbers, separated by spaces: ")
user_list = list(map(int, user_input.split()))

# Call the function with the user-defined list
result = sum_of_squares(user_list)
print("Sum of squares:", result)

