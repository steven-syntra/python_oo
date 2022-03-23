import matplotlib.pyplot as plt
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', index_col='date', parse_dates=True)

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Een kleurverloop gebruiken
ax.scatter(climate_change['co2'], climate_change['relative_temp'],
           c=climate_change.index)

ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")

plt.show()
