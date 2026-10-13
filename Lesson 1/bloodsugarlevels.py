import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 92, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

type = [blood_sugar_men, blood_sugar_women]
colors = ["#34D3DB", "#7700FFFF"]
label = ['men', 'women']
bins = [80, 100, 125, 150]
plt.xlabel('Blood Sugar Range', fontsize=12)
plt.ylabel("Total no. of patients", fontsize=12)

plt.hist(type, bins=bins, rwidth=0.95, edgecolor='black', linewidth=2, color=colors, label=label, orientation='horizontal')
plt.title("Blood Sugar Level Chart", fontsize=17)
plt.legend()
plt.show()