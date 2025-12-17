#count the number of vowels, consonants, digits, and special characters

s = input("enter string:")
vowels=consonants =digits=special=0
for ch in s:
    if ch.lower() in 'aeiou':
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1

print("vowels",vowels)
print("consonants",consonants)
print("digits",digits)
print("special",special)

#reverse string

words=s.split()
result=[]
for word in words:
    result.append(word[::-1])

print("".join(result))

#palindrome
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")


#frequency of each character

freq={}

for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

#modify a character and handling the error.

s="python"
try:
    s[0]='J'
except TypeError as e:
    print("error",e)