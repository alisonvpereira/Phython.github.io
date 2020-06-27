# Q1 Kate’s cat, Roary, loves catching moths. 
# Write a program that determines whether or not 
# it is time for Roary to catch moths.

print()
print("---------- Q1 ----------")
moths_in_house = False
if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")
print("------------------------")


#Q2 But Roary can’t actually get the moths by herself! 
# Amend the previous program to determine whether or 
# not it is time for Roary to go moth hunting.
print()
print("---------- Q2 ----------")
moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
else:
    print("Climb on Mitch")
print("------------------------")

# Q3 Write a program that implements the algorithm for Red Light Cameras.
print()
print("---------- Q3 ----------")
flash = ['Red']
light_colour = "Red"
car_detected = True

if light_colour in flash and car_detected:
    print("Flash!")
else:
    print("Do Nothing.")
print("------------------------")


# Q4 Write a program that asks the user for their height, and 
# determine whether or not they are tall enough to
# ride the rollercoaster, which has a height requirement of 120cms
print()
print("---------- Q4 ----------")

height = input("How tall are you in centimeters?: ")

if int(height) <= 120:
    print("Sorry, not today :(")
else:
    print("Hop on!")
print("------------------------")