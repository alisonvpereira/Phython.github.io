# Q1 Write a program that takes two numbers from the user, 
# and outputs their sum.
#1
print("------ Start of Q1 ------")
first_input = input("Enter a number: ")
second_input = input("Enter another number: ")
output = int(first_input) + int(second_input)
print(f"Your output is {output}")
print()

print("Round 2...")
print()

#2
first_input = input("Enter a number: ")
second_input = input("Enter another number: ")
output = int(first_input) + int(second_input)
print(f"Your output is {output}")
print()

print("Round 3...")
print()

#3
first_input = input("Enter a number: ")
second_input = input("Enter another number: ")
output = float(first_input) + int(second_input)
print(f"Your output is {output}")
print("------ End of Q1 ------")
print()


# Q2 Write a program that takes two numbers from the user, 
# and outputs the equation representing the multiplication of the two numbers.
# 1
print("------ Start of Q2 ------")
first_input = input("Enter a number: ")
second_input = input("Enter another number: ")
output = int(first_input) * int(second_input)
print(f"{first_input} * {second_input} = {output}")
print()

print("Round 2...")
print()

# 2
first_input = input("Enter a number: ")
second_input = input("Enter another number: ")
output = int(first_input) * int(second_input)
print(f"{first_input} * {second_input} = {output}")
print()

print("Round 3...")
print()

# 3
first_input = input("Enter a number: ")
second_input = input("Enter another number: ")
output = float(first_input) * int(second_input)
print(f"{first_input} * {second_input} = {output}")

print("------ End of Q2 ------")
print()

# Q3 Write a program that takes a distance in kilometers from the user, 
# and output the distance in meters andcentimeters.

#1
print("------ Start of Q3 ------") 
kms = input("Enter kilometers to convert: ")
meters = int(kms) * 1000
cms = int(kms) * 100000
print(f"{kms}km = {meters}m")
print(f"{kms}km = {cms}cm")
print()

print("Round 2...")
print()

#2
kms = input("Enter kilometers to convert: ")
meters = int(float(kms) * 1000)
cms = int(float(kms) * 100000)
print(f"{kms}km = {meters}m")
print(f"{kms}km = {cms}cm")

print("------ End of Q3 ------")
print()

# Q4 Write a program that takes the users name and height (in centimeters), 
# and outputs a summary sentence.

#1
print("------ Start of Q4 ------")
name = input("What is your name? ")
print(f"Hi {name}!")
height = input("How tall are you in centimeters? ")
print(f"{name} is {height}cms tall")
print()

print("Round 2...")
print()

#2
name = input("What is your name? ")
print(f"Hi {name}!")
height = input("How tall are you in centimeters? ")
print(f"{name} is {height}cms tall")
print("------ End of Q4 ------")