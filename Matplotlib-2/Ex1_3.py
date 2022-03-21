import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', index_col='date', parse_dates=True)

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()
