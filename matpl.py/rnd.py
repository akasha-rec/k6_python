import matplotlib.pyplot as plt
import random

# x = list(range(100))
# y = list(range(100, 200))

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(100, 200) for _ in range(100)]

rnd_x = [5, -5]
rnd_y = [5, -5]

x_data, y_data = [], []
x, y = 0, 0
x_data.append(x)
y_data.append(x)
rnd_walk = [[-5, 5, -5, 5][random.randint(0, 4)] for _ in range(100)]
print(rnd_walk)
for x_move, y_move in zip(rnd_x, rnd_y):
    x, y = x+x_move, y+y_move
    x_data.append(x)
    y_data.append(y)

# fig, ax = plt.subplots()
# ax.plot(x[:50], y[:50], color="red")
# ax.plot(x[50:], y[50:], color="blue")
# # ax.scatter(x[:50], y[:50], color="red")
# # ax.scatter(x[50:], y[50:], color="blue")
# plt.show()
