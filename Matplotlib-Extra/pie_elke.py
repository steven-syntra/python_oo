import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Rood', 'Groen', 'Blauw'
mycolors = ["r", "g", "b"]
sizes = [25, 30, 45]

fig1, ax1 = plt.subplots()
res1, labels, percentages = plt.pie(sizes, labels=labels, colors=mycolors, autopct="%1.0f%%", startangle=90)

for ins in percentages:
    ins.set_color('white')

for ins in labels:
    ins.set_color('orange')

ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

print(type(res1))
print(res1)
print(type(res2))
print(res2)
