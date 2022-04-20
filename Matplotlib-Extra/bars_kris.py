import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pandas as pd
import numpy as np

data = pd.read_csv('export3.csv', sep=";", index_col=0)
data_vl = data.loc["Vlaanderen", :]

women_vl = data_vl[data_vl["Gender"] == 'Women']
women_vl_pop = list(women_vl.loc[: , "Population"]) # [630037, 1976581, 752827]

men_vl = data_vl[data_vl["Gender"] == 'Men']
men_vl_pop = list(men_vl.loc[: , "Population"]) # [659950, 2009936, 623731]


age_groups = list(np.unique(data_vl["Age Group"])) # ['18-', '18-64', '65+']
x = np.arange(len(age_groups))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_vl_pop, width, label='Men', color='#301ee3')
rects2 = ax.bar(x + width/2, women_vl_pop, width, label='Women', color='#b0f68e')

ax.set_ylabel('Aantal')
plt.subplots_adjust(left=0.2)
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
ax.set_title('Bevolking Vlaanderen op 01/01/2021')
ax.set_xticks(x, age_groups)
ax.legend()
plt.show()