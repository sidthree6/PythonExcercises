# Ask user to input number and another number to divide it by
num = int(input("Please enter number: "))
check = int(input("Enter number to divide by: "))

# if number is divided by 2 evenly, its even number else its odd number
if num % 2 == 0:
    # another condition is number is also divided by 4
    if num % 4 == 0:
        print(num, " is even number & dividable by 4")
    else:
        print(num, " is even number")
else:
    print(num, " is odd number")

# check if number is divided evenly by other number user input
if num % check == 0:
    print(num, " is evenly divided by ", check)
else:
    print(num, " is not evenly divided by ", check)
