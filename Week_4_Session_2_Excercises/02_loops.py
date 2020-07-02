print("---------- Start Q1 ----------")
counter = 0
while counter < 3:
    num_list= []
    number = input("Enter a number: ")
    num_list.append(number)
    while len(num_list) > 0:
        if num_list[-1] != '':
            number = input("Enter a number: ")
            num_list.append((number))
        else:
            num_list.pop()
            num_list1 = list(map(int,num_list))
            print(sum(num_list1))
            num_list.clear()
            num_list1.clear()
    counter = counter + 1
    print()    
print("------------------------------")

print()
print("---------- Start Q2 ----------")
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]
for n in mailing_list:
    print(f"{n[0]}: {n[1]}")
print("------------------------------")

# print()
# print("---------- Start Q3 ----------")
# name_list= []
# counter = 0
# count = int(input("How many names? "))
# while counter < count:
#     name = input("Enter name: ")
#     name_list.append(name)
#     counter = counter + 1
#     # print(name)
# else:
#     for n in name_list:
#         print(n)    
# print("------------------------------")
    
print()
print("---------- Start Q3 ----------")
name_list= []
while len(name_list) < 3:
    name = input("Enter name: ")
    name_list.append(name)
else:
    print()
    print("Output: ")
    for n in name_list:
        print(f"   {n}")
print("------------------------------")

print()
print("---------- Start Q4 ----------")
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

for n in groceries:
    units = int(input(f"How many units of {n[0]}? "))
    cost = n[1] * units
    n.append(cost)
print()
print("====Izzy's Food Emporium====")
for n in groceries:
    cost = sum(n[-1] for n in groceries)
    print(f"{n[0]:<15} ${n[-1]:.2f}")

print("============================")
print(f"                ${cost:.2f}")
print()
print("------------------------------")






