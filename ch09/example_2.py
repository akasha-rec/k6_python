from random import randint

class Die:
    def __init__(self, sides = 6): #기본값이 6인 sides 속성
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

dice6 = Die()
results = []
for num in range(10):
    result = dice6.roll_die() #6면체를 던진 결과
    results.append(result) #를 모은 리스트
    print(results)

dice10 = Die()
results = []
for num in range(10):
    result = dice10.roll_die() #10면체을 던진 결과
    results.append(result) #를 모은 리스트
    print(results)