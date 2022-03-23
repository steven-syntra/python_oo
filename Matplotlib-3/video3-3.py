import pandas as pd
import matplotlib.pyplot as plt

mens_rowing = pd.read_csv('mens_rowing.csv', index_col=0)
mens_gymnastic = pd.read_csv('mens_gymnastic.csv', index_col=0)

fig, ax = plt.subplots()

ax.boxplot([mens_rowing["Height"], mens_gymnastic["Height"]])
ax.set_xticklabels(["Rowing", "Gymnastics"])
ax.set_ylabel("Height (cm)")

plt.show()

