from matplotlib import pyplot as plt
from random import randint
# print(randint(0, 9)) 0~9까지 난수 생성

x1 = list(range(1, 5))
y1 = [i*i for i in x1]

x2 = list(range(1, 5))
y2 = [i**3 for i in x2]

# fig, axs = plt.subplots(1, 2)
# axs[0].plot(x1, y1)
# axs[0].plot(x2, y2)

# axs[1].scatter(x1, y1)
# axs[1].scatter(x2, y2) 

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title("X square")
plt.xlabel("X")
plt.ylabel("X square")
# x = [1, 2, 3, 4]
# y = [i**2 for i in x]
# print(type(x), x)
# print(type(y), y)

# plt.plot(x, y) (x, y) 선 표현 
# plt.scatter(x, y) #(x, y) 점으로
# x = [randint(0, 9) for i in range(100000)]
# plt.hist(x) x만 있어도 가능
