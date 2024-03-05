travel = ["Japan", "Europe", "Amazon", "Seoul", "Finland"]
print(travel)
print(sorted(travel)) #print(sorted(리스트명))
#print(sorted(리스트명, reverse=True)) : 역순
print(sorted(travel, reverse=True)) 
travel.reverse() #리스트명.reverse() : 현재 리스트 순서 반대로
print(travel)
travel.reverse() #리스트명.reverse() : 현재 리스트 순서 반대로
print(travel)
travel.sort() #리스트명.sort() : 영구 정렬 > 원래 순서로 돌아가지 X 
print(travel)
travel.sort(reverse=True) # sort로 역순 출력
print(travel)

party = ["A", "B", "C"]
print(f"{party[0]}을 파티에 초대합니다.")
print(f"{party[1]}을 파티에 초대합니다.")
print(f"{party[2]}을 파티에 초대합니다.")
print(f"파티에 {len(party)}명이 초대되었습니다.")