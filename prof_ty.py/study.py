a = {1 : "a", 2 : "b", 3 : "c"} # dictionary {}
b = [1, 2, 3] # list[]
c = (1, 2, 3) # tuple()
print(type(a))
print(type(b))
print(type(c))

A = {"a" : 1, "b" : 2, "c" : 3}
A["d"] = 4 #append 사용하지 않고도 추가
A["c"] = 6 #변경도 가능
print(A)

# d = {"Name" : "Grade", "정원" : "A+", "윤정" : "A+", "세영" : "A+"}
db = {
     7 : {7, "정원", "A+"}, 
     9 : {9, "윤정", "A+"}, 
     8 : {8, "세영", "A+"}
     }
print(db)
# if 4 in db: 방어적 코드?
#     db[4]
print(db.get(3))
print(db.get(4)) #return None

for row in db:
    print(row)

for row in db.items():
    print(row)

e = [3, 2, 1]
print(sorted(e))

print(sorted(db.items())) #dictionary도 정렬 가능

gr = {
     7 : "C", 
     9 : "A", 
     8 : "B"
     }

#성적순 정렬 ??
first = lambda x:x[0]
second = lambda x:x[1]
for row in gr.items():
    print(first(row), second(row))

sorted(gr.items(), key=second)

#중첩
for x in range(5):
    for y in range(10):
        print(x, y)

lst = [[1, 2, 3], [4, 5, 6]]
print(lst)

d1 = {
    "a" : {
        "A" : "b"
    },
    "b" : []
}
print(d1)

db2 = {}
#dic[key] = value 접근
db2["a"] = list() # 키 a - 값 list
db2["a"].append(3)
db2["a"].append("A")
db2["a"].append("B+")
print(db2)

def add(a, b):
    return a+b
print(add(1, 2))

data = {"a" : 1, "b" : 2, "c" : 3}
print({v : k for k, v in data.items()}) # key-value > value-key
print({x**2 for x in range(5) if x % 2 ==0})
