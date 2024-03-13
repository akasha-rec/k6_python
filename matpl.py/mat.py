import matplotlib.pyplot as plt

fig, ax = plt.subplots() #여러 개의 그래프를 하나의 그림에 나타내도록
x1 = [1, 2, 3, 4]
y1 = [2, 3, 4, 6]
# ax.plot(x1, y1, label="blue") 선 표현
ax.scatter(x1, y1, label="blue") #점 표현

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
# ax.plot(x2, y2, label="orange") 선 표현
ax.scatter(x2, y2, label="orange") #점 표현

ax.set_title('Plot A and B') #제목 표현
ax.set_aspect('equal')
ax.set_xlabel('Age') # 범례
ax.set_ylabel('BMI')
ax.set_xlim(0, 10) #축 세팅(0~10)
ax.set_ylim(0, 10)
ax.legend() #범례 추가하는 메서드
plt.savefig('plotprac.png') #저장
plt.show()