print("-------------------- Start Q1 --------------------")
foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[:3])
print(foods[-3:])
print(foods[-4][-1])
print("--------------------------------------------------")
print()

print("-------------------- Start Q2 --------------------")
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]
for n in mailing_list:
    print(f"{n[0]}: {n[-1]}")
print("--------------------------------------------------")
print()

print("-------------------- Start Q3 --------------------")
counter = 0
name_list = []
while counter < 3:
    name = input("Enter a name: ")
    name_list.append(name)
    counter = counter + 1
print() 
print(name_list)
print("--------------------------------------------------")
print()


print("-------------------- Start Q4 --------------------")
counter = 0
while counter < 2:
    sentence = input("Enter a string: ")
    words = sentence.split()
    letters = list(sentence)
    counter = counter + 1 
    print(f"{len(words)} {words}")
    print(f"{len(letters)} {letters}")
    print()
print("--------------------------------------------------")
print()