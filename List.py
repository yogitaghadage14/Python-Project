#Remove duplicate element from a list without using set

Lst=[1,2,3,4,5,2,4]
new_list=[]
for i in Lst:
    if i not in new_list:
        new_list.append(i)

print(new_list)


#create a list of even no using comprehension

Lst=[1,2,3,4,5,6]
even_list=[i for i in Lst if i%2==0]
print(even_list)

#find second largest elemnet

Lst=[1,2,3,433,45]
largest=second=Lst[0]

for i in Lst:
    if i>largest:
        second=largest
        largest=i
    elif i!=largest and i>largest:
        second=i
print(second)

#nested list and sum

Lst=[[1,2,3],[4,5],[6,7,8]]
for inner in Lst:
    print(inner)

#shallow copy

import copy
original=[[1,2],[3,4]]
shallow =original.copy()
deep=copy.deepcopy(original)
original[0][0]=99
print(original)
print(shallow)
print(deep)
