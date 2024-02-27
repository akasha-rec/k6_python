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
print(f"{party[1]}은 참가하지 못했습니다")



