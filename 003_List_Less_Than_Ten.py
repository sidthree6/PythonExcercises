# initialize list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# new list to store
b = []

# get a number from user
userNum = int(input("Please enter a number: "))

# Append a number to new list if it is less than user entered number
for x in a:
    if x < userNum:
        b.append(x)

print("Numbers less than ", userNum, " in list are...")

# print all numbers
for y in b:
    print(y)
