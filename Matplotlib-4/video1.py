import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.read_csv('seattle_weather.csv')
austin_weather = pd.read_csv('austin_weather.csv')

# Use ggplot style
plt.style.use("ggplot")

fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])

ax.set_xlabel("Time (months)")
ax.set_ylabel("Average Temperature (Fahrenheit degrees)")

plt.show()

