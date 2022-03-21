import pandas as pd

climate_change = pd.read_csv('climate_change.csv', index_col='date', parse_dates=True)

print(climate_change.index)

