import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv('medals.csv', index_col=0)
fig, ax = plt.subplots()

# alle kolommen toevoegen, met label
ax.bar(medals.index, medals["Gold"], label="Gold")
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver" )
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")

ax.set_xticklabels(medals.index, rotation=90)
ax.set_ylabel("Number of medals")

# ook de legende toevoegen
ax.legend()
plt.show()


