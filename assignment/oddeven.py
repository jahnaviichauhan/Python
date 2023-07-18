import random
numbers = [random.randint(1, 100) for _ in range(10)]
odd_list = [num for num in numbers if num % 2 != 0]
even_list = [num for num in numbers if num % 2 == 0]
print("Original list:", numbers)
print("Odd list:", odd_list)
print("Even list:", even_list)
