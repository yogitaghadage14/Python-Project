#maximum and minimum elements in a tuple.

t=(4,9,1,7,3)
max_val=t[0]
min_val=t[0]

for i in t:
    if i>max_val:
        max_val=i
    if i<min_val:
        min_val=i

print("max_val",max_val)
print("min_val",min_val)

#list of tuples into a dictionary.

Lst=[("a",1),("b",2),("c",3)]
d={}

for key, value in Lst:
    d[key]=value

print(d)

#Count the occurrence of an element in a tuple without using built-in methods.
t=(1,2,3,2,4,2)
x=2
count=0
for i in t:
    if i==x:
        count+=1
print(count)


#Create a tuple with mutable elements and modify the mutable data inside it.

t=(1,2,[3,4])
t[2][0]=99
print(t)

#swap two tuple
t1=(1,2,3)
t2=(4,5,6)
t1,t2=t2,t1
print("t1:",t1)
print("t2:",t2)
