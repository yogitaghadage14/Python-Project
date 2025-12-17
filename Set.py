#union,itersection,diff,symmetric diff

s1={1,2,3,4}
s2={3,4,5,6}
print("union:",s1.union(s2))
print("intersection:",s1.intersection(s2))
print("difference:",s1.difference(s2))
print("symmetric_difference:",s1.symmetric_difference(s2))


#remove comm element from two sets

common=s1 & s2
s1=s1-common
s2=s2-common

print("s1:",s1)
print("s2:",s2)


#check wheather one set is subset of snother

s3={3,4}

is_subset=True
for x in s3:
    if x not in s2:
        is_subset=False
        break

print("subset" if is_subset else "not subset")


#print element of greater that a given no

s={10,5,20,15,3}
y=10

for i in s:
    if i>y:
        print(i)


#convert list with duplicate set

Lst=[1,2,3,2,4,1,5]

unique_list=list(set(Lst))
print(unique_list)

