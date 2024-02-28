cars = ["bmw", "audi", "toyota", "subaru"]
for car in cars: #확장형 for문, loop block안에 있는 건 모두 for문으로 간주
    print(car)
    print(f"my car is a {car}")
print("리스트 출력 완료")

for car2 in cars:
    print("my car\n")
    for c2 in cars:
        print()

print("for문 종료")