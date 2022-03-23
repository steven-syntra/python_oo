import matplotlib.pyplot as plt
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', index_col='date', parse_dates=True)
eighties = climate_change["1980-01-01":"1989-12-31"]
nineties = climate_change["1990-01-01":"1999-12-31"]

# Initalize a Figure and Axes
fig, ax = plt.subplots()

ax.scatter(eighties['co2'], eighties['relative_temp'], color="r", label="eighties")
ax.scatter(nineties['co2'], nineties['relative_temp'], color="b", label="nineties")

ax.legend()

ax.set_xlabel("CO2 (ppm)")
ax.set_ylabel("Relative temperature (Celsius)")

plt.show()
