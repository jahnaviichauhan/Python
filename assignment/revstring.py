def reverse_string(string):
    reversed_string = ""
    for index in range(len(string)-1, -1, -1):
        reversed_string += string[index]
    return reversed_string
string = input("Enter a string: ")
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)
