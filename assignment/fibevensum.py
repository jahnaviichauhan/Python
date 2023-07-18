def fibonacci_sum_even(n):
    fibonacci_sequence = [0, 1]
    sum_even = 0

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
        if next_term % 2 == 0:
            sum_even += next_term

    return fibonacci_sequence, sum_even
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
sequence, sum_even = fibonacci_sum_even(n)
print("Fibonacci sequence:", sequence)
print("Sum of even-valued terms:", sum_even)

