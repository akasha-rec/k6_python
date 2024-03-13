import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()

data = [random.randint(0, 100) for _ in range(1000)]
ax.hist(data) #도수분포표 그려주는 메서드
plt.show()