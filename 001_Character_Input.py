# import datetime to get current year for calculation
import datetime

# Get name and age of user
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# calculate year when user will be 100 years old based on age input
now = datetime.datetime.now()
year = str((now.year - age) + 100)

# store and print message
message = name + " will be 100 years old in " + year

print(message)

# asks user how many times message will repeat
loop = int(input("How many times do you want to repeat this message: "))

# run loop for amount of times user have entered and print message
for x in range(loop):
    print(message)
