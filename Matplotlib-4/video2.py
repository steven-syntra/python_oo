import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv('medals.csv', index_col=0)
fig, ax = plt.subplots()

ax.bar(medals.index, medals["Gold"])
ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")

# set width, height
fig.set_size_inches([5,5])

# adjust bottom space
plt.subplots_adjust(bottom=0.30)

# save to PNG
fig.savefig("gold_medals.png", dpi=150)
