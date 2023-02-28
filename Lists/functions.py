#Program to perform functions on list

lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = (input())
  
    # adding the element
    lst.append(ele) 
      
n=len(lst)
print("Length of list:", n) #Prints length of list

print(lst[0])#Prints first element

print(lst[n-1])# Prints last elemen t

print(lst[-1])#Prints last element, moves from right to left with -1 being the last

print(lst[-n])#Prints first element, moves from left to right with -n being the first

print(lst)#Prints list

print(lst[0:4])#Prints list from 0 till 4-1, i.e. 3

print(lst[1:])#Prints elements from the second member to last

print(lst[:3])#Prints elements till the third member, i.e. till 2

print(lst[:])#Prints the entire list

print(lst[:-1])#Prints the whole list except the last ONE member

print(lst[-1:])#Prints one of the last two members excluding the last one

print(lst[-2:])#Prints two of the last three members excluding the last one

print(lst[:-2])#Prints the whole list except the last TWO members

print(lst[::-1])#Prints reverse of list

print(lst[2::-1])#Prints reverse of first three members