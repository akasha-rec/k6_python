# with open('a.csv') as f:
#     for line in f:
#         print(line.rstrip().split(","))

# from pathlib import Path
from matplotlib import pyplot as plt
import csv

x, y = [],[]
x1, y1 = [],[]
COL_DATE = 2
COL_TMAX = 4

# with open(Path("data", "a.csv")) as f:
with open("a.csv") as f:
    reader = csv.reader(f)
    header = next(reader) #header 제외 출력
    for line in reader:
        # print(line) <class 'list'>

        x.append(line[COL_DATE])
        y.append(line[COL_TMAX])
        x1.append(line[COL_DATE])
        y1.append(line[5])

# for h in header:
#     print(h)
for idx, h in enumerate(header):
    print(idx, h)

print(f"x: {x1}")
print(f"y: {y1}")
# plt.title("TMAX")
plt.plot(x, y, label="TMAX")
plt.plot(x1, y1, label="TMIN")
plt.legend()
plt.show()
