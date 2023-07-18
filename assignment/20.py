def find_numbers():
    numbers = []
    for num in range(1000, 2000):
        digits = str(num)
        odd_place_sum = sum(int(digit) for digit in digits[1::2])
        if all(int(digit) % 2 == 0 for digit in digits[1::2]) and odd_place_sum not in numbers:
            numbers.append(odd_place_sum)
    return numbers

# Find numbers and their unique sums
number_list = find_numbers()
unique_sums = len(number_list)

print("Numbers:", number_list)
print("Unique sums:", unique_sums)

