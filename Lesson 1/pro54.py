import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 13)

y1 = x * 500
y2 = x * 700 

plt.plot(x, y1, 'g', linestyle='dashed', marker='o', label='500')
plt.plot(x, y2, 'r', marker='D', label='700')
plt.fill_between(x, y1, y2, alpha=0.3, label='Difference')

plt.title('Savings Chart')
plt.xlabel('Month')
plt.ylabel('Total Savings')

plt.xlim(1, 12)
plt.ylim(0, 9000)

plt.legend(loc='upper right')
plt.show()