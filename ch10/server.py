from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path("numbers.json") #리스트를 저장할 파일 이름 지정
contents = json.dumps(numbers)#json.dump() > JSON 문자열로 변환
path.write_text(contents)