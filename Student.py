#create student.txt and write

with open("student.txt","w") as f:
    f.write("1,Yogita\n")
    f.write("2,manu\n")
    f.write("3,siya\n")


#read and display

with open("student.txt","r") as f:
    print(f.read())

#append

with open("student.txt","a") as f:
    f.write("4,amol\n")


#count
with open("student.txt","r") as f:
    print(len(f.readlines()))

#search

name=input("Enter your name:")
with open("student.txt","r") as f:
    for line in f:

        if name in line:
            print(line)