import datetime
from datetime import datetime as dt

today = dt.strptime("2024-03-15", "%Y-%m-%d") #형식 문자열을 받아 날짜 해석
print(today + datetime.timedelta(days=3)) #날짜 연산

#java의 try-catch > python에서는 try-except
try:
    with open("c.csv") as f:
        for line in f:
            print(line)
except Exception as e:
    # pass
    print(e) #오류메시지 출력