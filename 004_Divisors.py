# get a number from user
num = int(input("Please enter a number: "))

# create a list randing from 1 to user entered number
listDivisor = range(1, num+1)

# create empty list
divisor = []

# check if number is divisors and append to list
for number in listDivisor:
    if num % number == 0:
        divisor.append(number)

# print list
print(divisor)
