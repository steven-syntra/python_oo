import pandas as pd
import matplotlib.pyplot as plt

mens_rowing = pd.read_csv('mens_rowing.csv', index_col=0)
mens_gymnastic = pd.read_csv('mens_gymnastic.csv', index_col=0)

fig, ax = plt.subplots()

ax.bar("Rowing",
       mens_rowing["Height"].mean(),
       yerr=mens_rowing["Height"].std())
ax.bar("Gymnastics",
       mens_gymnastic["Height"].mean(),
       yerr=mens_gymnastic["Height"].std())

ax.set_ylabel("Height (cm)")

plt.show()

