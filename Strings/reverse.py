#Program to reverse words in a given string

#Inputting string
s=input("Enter string")

s = string.split()[::-1]
l = []

for i in s:
    #apending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))