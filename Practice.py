#even no

def get_even_numbers(nums):
    return [n for n in nums if n%2==0]
print(get_even_numbers([1,2,3,4,5,6]))


#character count
def char_count(s):
    d={}
    for i in s:d[i]=d.get(i,0)+1
    return d
print(char_count("abc"))

#palindrome no
def is_palindrome(n):
    return str(n)==str(n)[::-1]
print(is_palindrome(5))

#average using *args

def avg(*args):
    return sum(args)/len(args)
print(avg(1,2,3,4,5,6))

#common elements (no set)

def common(Lst1,Lst2):
    return [x for x in Lst1 if x in Lst2]
print(common([1,2,3,4,5,6],[5,6,7,8,9,10]))