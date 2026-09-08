import matplotlib.pyplot as plt

temperature = [20, 22, 25, 23, 27]
days = [1, 2, 3, 4, 5]

plt.plot(days, temperature)

plt.title("Temperature Over 5 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")

plt.show()