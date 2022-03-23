import pandas as pd
import matplotlib.pyplot as plt

mens_rowing = pd.read_csv('mens_rowing.csv', index_col=0)
mens_gymnastic = pd.read_csv('mens_gymnastic.csv', index_col=0)

fig, ax = plt.subplots()

ax.hist(mens_rowing["Height"], label="Rowing")
ax.hist(mens_gymnastic["Height"], label="Gymnastics")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Nr of observations")

ax.legend()
plt.show()

