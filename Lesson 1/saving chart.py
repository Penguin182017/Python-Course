import matplotlib.pyplot as plt

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6']
savings = [500, 800, 1200, 1500, 1900, 2300]

plt.plot(
    weeks,
    savings,
    marker='o',
    linestyle='-',
    linewidth=2,
    label="Weekly Savings"

)

plt.title("My Savings Project")
plt.xlabel("Weeks")
plt.ylabel("Savings ($)")
plt.grid(True)
plt.legend()

plt.show()

plt.bar(
    weeks,
    savings,
    label='Weekly Savings'

)

plt.title("Weekly Savings Comparison")
plt.xlabel("Weeks")
plt.ylabel("Savings ($)")
plt.legend()
