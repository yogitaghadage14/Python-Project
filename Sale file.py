#create sales.txt and store data

with open("sales.txt","w") as f:
    f.write("101,500\n")
    f.write("102,700\n")

#append
Student
with open("sales.txt","aSt") as f:
    f.write("103,300\n")


#convert sales.txt to sales.csv

import csv
with open("sales.txt","r") as txt,open("sales.csv","w",newline="") as csvf:
    writer = csv.writer(csvf)
    writer.writerows(["saleid","amount"])
    for line in txt:
writer.writerrow(line.strip().split(","))


#read and display

import csv
with open("sales.txt","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#calculate total sale amount

import csv
total=0
with open("sales.txt","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total+=int(row["amount"])
print(total)

