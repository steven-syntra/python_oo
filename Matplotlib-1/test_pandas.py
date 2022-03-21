import pandas as pd

seattle_weather = pd.read_csv('seattle_weather.csv')
print(seattle_weather["MLY-PRCP-NORMAL"])

