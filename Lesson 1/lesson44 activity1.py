import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [75, 85, 60, 90, 75]
plt.plot(days, scores)
plt.show()

plt.plot(days, scores)
plt.title("My Quiz Score Tracker")
plt.xlabel("Day of The Week")
plt.ylabel("Score")
plt.grid(True)
plt.ylim(0, 100)
plt.show()

plt.plot(days, scores, color='blue', marker='o', linestyle='dashed', linewidth=2)
plt.title("My Quiz Score Tracker")
plt.xlabel("Day of the Week")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.show()

plt.bar(days, scores, color='blue')
plt.title("My Quiz Score Tracker")
plt.xlabel("Day of the Week")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.show()
