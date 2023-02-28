#Program to traverse a list using indexing

lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = (input())
  
    # adding the element
    lst.append(ele) 
   
#Traversing using indexing; Adding a done at the emd of
for i in range(0,n):
    lst[i]=lst[i]+' done'
    
print(lst)