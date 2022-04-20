# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

population = pd.read_csv('export3.csv', delimiter=";", index_col=0)

vla = population[population.index == "Vlaanderen"]
vla_men = vla[vla["Gender"] == "Men"]
vla_women = vla[vla["Gender"] == "Women"]

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

ax.bar([0, 2, 4], vla_men["Population"], width=0.6, label="Mannen", color="blue")
ax.bar([0.6, 2.6, 4.6], vla_women["Population"], width=0.6, label="Vrouwen", color="lightgreen")

# set x axis labels
plt.xticks([0.3, 2.3, 4.3], vla_men["Age Group"])

# Finish
ax.set_title("Bevolking Vlaanderen op 1/1/2021")
ax.set_ylabel("Aantal")

# format y-axis ticks
plt.ticklabel_format(axis='y', style='plain', useLocale=True)
ax.get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, loc: format(x, "6,.0f").replace(",", ".")))

# more margin left
plt.subplots_adjust(left=0.20)

# add legend
ax.legend()
plt.show()
