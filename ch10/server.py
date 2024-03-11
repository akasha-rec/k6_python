# from pathlib import Path
# import json

# numbers = [2, 3, 5, 7, 11, 13]

# path = Path("numbers.json") #리스트를 저장할 파일 이름 지정
# contents = json.dumps(numbers)#json.dump() > JSON 문자열로 변환
# path.write_text(contents)


import json
#json.loads(data) : String인 JSON 데이터를 딕셔너리로 로드
#json.dump(json.loads(data), w_file) : 파이썬 객체를 JSON 형식으로 인코딩
#딕셔너리 형식의 JSON 데이터가 저장
data = '{"name":"Kim", "age":23}'
with open('member.json', 'w') as w_file:
    json.dump(json.loads(data), w_file)

member = '{"name":"Lee", "age":24}'
with open('member2.json', 'w') as w_file:
    json.dump(json.loads(member), w_file)

# {'name': 'Lee', 'age': 24} <class 'dict'>
with open('member2.json', 'r') as r_file:
    d = json.load(r_file)
    print(d, type(d))

# {"name": "Lee", "age": 24} <class 'str'>
#파이썬 객체를 JSON 형식의 문자열로 인코딩
d2 = json.dumps(json.loads(member))
print(d2, type(d2))

# {'name': 'Lee', 'age': 24} <class 'dict'> Lee
d3 = json.loads(d2)
print(d3, type(d3), d3["name"])

#파일의 입출력에 사용
#json.dump(obj, file) : 파이썬 객체 obj를 JSON 형식으로 인코딩해서 파일에 씀
#json.load(file) : 파일에서 JSON 형식의 데이터를 읽어와 파이썬 객체로 디코딩

#문자열을 다룰 때 사용
#json.dumps(obj) : obj를 JSON 형식으로 인코딩해서 문자열 반환
#json.loads(s) : JSON 형식의 문자열 s를 읽어와서 파이썬 객체로 디코딩
