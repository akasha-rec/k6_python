name = "eric"
print(f"안녕하세요. {name}, 오늘 파이썬 배워보는 건 어떨까요?")

person_name = "hyun"
print(person_name.upper())
print(person_name.lower())
print(person_name.title())

famous_person = "이순신"
print(f'{famous_person}, "신에게는 아직 {12}척의 배가 남아있습니다."')
message = f'{famous_person}, "신에게는 아직 {12}척의 배가 남아있습니다."'
print(message)

name = "\t에릭\n마틴\t"
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

# 연습문제 3-4
party = ["A", "B", "C"]
print(f"{party[0]}을 파티에 초대합니다.")
print(f"{party[1]}을 파티에 초대합니다.")
print(f"{party[2]}을 파티에 초대합니다.")

# 연습문제 3-5 p85
print(f"{party[1]}을 파티에 오지 못한다고 합니다.")
del(party[1])
party.insert(1, "D") #원하는 위치에 삽입하기 위해서 (idx, 요소)

print(f"{party[0]}을 파티에 초대합니다.")
print(f"{party[1]}을 파티에 초대합니다.")
print(f"{party[2]}을 파티에 초대합니다.")
# print(party)
print("큰 테이블을 찾았어요")
party.insert(0, "가")
party.insert(2, "나")
party.append("다")
# print(party)

print(f"{party[0]}을 파티에 초대합니다.")
print(f"{party[1]}을 파티에 초대합니다.")
print(f"{party[2]}을 파티에 초대합니다.")
print(f"{party[3]}을 파티에 초대합니다.")
print(f"{party[4]}을 파티에 초대합니다.")
print(f"{party[5]}을 파티에 초대합니다.")

print("죄송하지만 2명만 가능합니다")
party.pop()
party.pop()
party.pop()
party.pop()
print(party)

del(party[0]) #del[] < 인덱스로 접근, 재사용X
del(party[0]) #바로 제거되니까 반복
print(party)

