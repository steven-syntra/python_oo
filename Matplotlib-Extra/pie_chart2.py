import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Rood', 'Groen', 'Blauw'
sizes = [25, 30, 45]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=["r", "g", "b"], autopct='%1.0f%%', shadow=False, startangle=90, textprops={'color':"white", 'size':20})
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
