import matplotlib.pyplot as plt

bars1 = [12, 28, 1, 8, 22]
bars2 = [28, 7, 16, 4, 10]

# The position of the bars on the x-axis
r = [0,1,2,3,4]

# Names of group and bar width
names = ['A','B','C','D','E']
barwidth = 1

# Create brown bars
plt.bar(r, bars1, color="#51d9ff", edgecolor='white', width=barwidth)
# Create green bars (middle), on top of the first ones
plt.bar(r, bars2, bottom=bars1, color="#0091ff", edgecolor='white', width=barwidth)

# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("group")

# Show graphic
plt.show()