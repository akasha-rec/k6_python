from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

name = ["hong", "lee", "kang"]
values1 = [50, 70, 20]
values2 = [30, 50, 70]

index = np.arange(3)
df = pd.DataFrame({"korean":values1, "eng":values2}, index=name)
df

fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.25
b1 = plt.bar(index, df["korean"], bar_width, alpha=0.4, color="red", label = "korean")
b2 = plt.bar(index+bar_width, df["eng"], bar_width, alpha=0.4, color="blue", label = "eng")
plt.xticks(np.arange(bar_width, 3 + bar_width, 1), name)

plt.xlabel("name")
plt.ylabel("grade")
plt.legend()
plt.show()

#https://jimmy-ai.tistory.com/40