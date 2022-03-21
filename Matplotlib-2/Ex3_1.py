import matplotlib.pyplot as plt
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', index_col='date', parse_dates=True)

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate( ">1 degree", xy=(pd.Timestamp("2015-10-06"), 1))

plt.show()