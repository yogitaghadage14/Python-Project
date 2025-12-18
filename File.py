#create attendance file and write data
import csv

with open("attendance.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["ID","Name","status"])
    writer.writerow([1, "anu", "present"])
    writer.writerow([2, "anitha", "present"])

#read and display

import csv
with open("attendance.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


#append attendance record

import csv
with open("attendance.csv","a") as f:
    writer = csv.writer(f)
    writer.writerow(["103","Rohit","present"])



#count absent emp

import csv
count=0
with open("attendance.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row["status"]=="absent":
            count+=1
print(count)


#search emp using id

import csv
eid=input("enter attendance ID")
with open("attendance.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row["ID"]==eid:
            print(row)
            
