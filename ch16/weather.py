from matplotlib import pyplot as plt
import csv
from datetime import datetime

x1 = []
y1 = []
y2 = []
with open("a.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader) #header만 뺴기
    print(header)
    for row in reader:
        x1.append(datetime.strptime((row[2]), "%Y-%m-%d")) # <class 'str'>
        y1.append(int(row[4]))
        y2.append(int(row[5]))

plt.fill_between(x1, y1, y2, alpha=0.5)
plt.xticks(x1, rotation="vertical")
plt.plot(x1, y1, label="TMAX", color="red")
plt.plot(x1, y2, label="TMIN", color="blue")
plt.title("X square")
plt.xlabel("X")
plt.ylabel("X square")
plt.legend()
plt.show()