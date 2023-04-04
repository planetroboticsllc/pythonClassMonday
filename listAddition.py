# ask user for a number
# create a list of all numbers from 1 to the user number
# all all numbers from this list
# print the addition
# print multiplication of all numbers
end = int(input("Enter a number: "))
numList = range(1, end)
sum = 0
for num in numList:
    sum = sum + num

print(f"Addition of all numbers: {sum}")

#print(f"Multiplication of all numbers is {product}")



