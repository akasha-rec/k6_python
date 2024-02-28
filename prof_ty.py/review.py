a = [1, 2, 3, 4, 5]
b = list()
print(type(a))
print(type(b))

s = "abcde"
print(s[:2], s[2:])
# len 리스트 길이
print(len(s))
print(type(s[:2])) 

# <class 'str'>
for s in "abcdef":
    print(s)

# range
for i in range(1, 6):
    print(i)

# class 'tuple' 
for a in (1, 2, 3, 4, 5):
    print(a)

for i in range(1, 6):
    if (i % 2 == 0):
        print(i, "even")
    else:
        print(i, "odd")