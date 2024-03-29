with open("galaxy.txt") as file:
    for line in file.readlines():
        print(line.rstrip())

print("A", end="") #end="" 개행 방지
print("B")

def add(a = 1, b = 2):
    return a+b
print(add())

# import csv
# with open('grade.csv') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     print(next(reader))
#     print(next(reader))
#     print(next(reader))
#     print(next(reader))
#     # for line in reader:
#     #     print(line)
#     # print(header)

# n = range(5)
# r = iter(n)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

import os

from pathlib import Path
#개발 환경은 윈도우(\)인데 배포할 때는 리눅스 서버(/)

#현재 작업 디렉토리에서 "경로"를 나타내는 Path 객체
dir_path = Path("./aaa")
print(dir_path)

file_path = Path("./aaa/a.txt")
print(file_path)

#★★★★★★★★
print(os.path.split(Path("./aaa/b.txt")))
# ('aaa', 'b.txt') ★★★★★★★★

print(os.path.isdir(dir_path))
print(os.path.isdir(file_path))

#현재 작업 디렉토리에 있는 모든 항목에 대해 반복
for d in os.listdir():
    print(d, os.path.isdir(d))

#파일 생성하기
# path = Path("./aaa/aa.txt")

# with open(path, "w") as file:
#     file.write("a\n")
#     file.write("ab\n")
#     file.write("abc\n")

path = Path("./aaa/aaa.txt")
try: #방법 2
# 1. if path.exists(): #파일이 없어도 에러메시지가 안 나와 > 방어적 코드
    with open(path) as file:
        for line in file:
            print(line)

except Exception as e:
    pass