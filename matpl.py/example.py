import matplotlib.pyplot as plt

x = list(range(1, 101))
square = [i**2 for i in x]

#머신러닝 시각화할 때 많이 사용 > surface cmap > 3차원 표현
plt.scatter(x, square, c=square, cmap=plt.cm.Blues)

# ax.set_title("Square")
# ax.tick_params(labelsize=14)
plt.colorbar()
plt.savefig('colormap.png')
plt.show()