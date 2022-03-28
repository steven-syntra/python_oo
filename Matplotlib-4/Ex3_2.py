import pandas as pd
import matplotlib.pyplot as plt

summer_2016_medals = pd.read_csv('summer_2016_medals.csv')

# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
    # Extract the rows only for this sport
    sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
    # Add a bar for the "Weight" mean with std y error bar
    ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
plt.subplots_adjust(bottom=0.40)
fig.savefig("sports_weights.png")
