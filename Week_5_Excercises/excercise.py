print("-------------------- Q1 --------------------")
names = []
with open("names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)


for index,line in enumerate(names):
    print(f"{index+1}. {line}")

print("------------------------------------------------------")
print()

print("------------------------- Q2 -------------------------")
import csv
colours = []
h = []
header = []
print("--------------------- colours_20 ---------------------")
with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    h = next(reader)

    for line in reader:
        # print(line)
        colours.append(line)

for line in h:
    # print(line.lstrip())
    header.append(line.lstrip())

colours.insert(0,header)

for l in colours:
    print(f"{l[1]:<15}  {l[2]:<15}  {l[4]}")

print("--------------------- colours_213 ---------------------")
import csv
colours = []
h = []
header = []

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    h = next(reader)

    for line in reader:
        # print(line)
        colours.append(line)

for line in h:
    header.append(line.lstrip())

colours.insert(0,header)

for l in colours:
    print(f"{l[1]:<15}  {l[2]:<15}  {l[4]}")

print("------------------------------------------------------")

print()
print("------------------------- Q3 -------------------------")
print("--------------------- colours_20 ---------------------")
import csv
colours = []

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for line in reader:
        # print(line)
        colours.append(line[4])

print(f"Red: {sum(x.count('red') for x in colours)}")
print(f"Green: {sum(x.count('green') for x in colours)}")
print(f"Blue: {sum(x.count('blue') for x in colours)}")

print("--------------------- colours_213 ---------------------")
import csv
colours = []

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for line in reader:
        # print(line)
        colours.append(line[4])

print(f"Red: {sum(x.count('red') for x in colours)}")
print(f"Green: {sum(x.count('green') for x in colours)}")
print(f"Blue: {sum(x.count('blue') for x in colours)}")
print("------------------------------------------------------")