toppers = [
    ["John", 95],
    ["Emma", 98],
    ["Michael", 92],
    ["Sophia", 96]
]
print("Initial Toppers Details:")
for topper in toppers:
    print("Name:", topper[0])
    print("Score:", topper[1])
    print()
index = int(input("Enter the index of the topper you want to edit (0 to {}): ".format(len(toppers)-1)))
if index >= 0 and index < len(toppers):
    name = input("Enter the updated name: ")
    score = int(input("Enter the updated score: "))
    toppers[index][0] = name
    toppers[index][1] = score
    print("Details updated successfully!")
else:
    print("Invalid index provided.")
print("\nUpdated Toppers Details:")
for topper in toppers:
    print("Name:", topper[0])
    print("Score:", topper[1])
    print()
