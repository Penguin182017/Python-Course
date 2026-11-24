import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Weather Dataset.csv')

data.head()

data_group = data.groupby('month').mean(numeric_only=True)
data_group = data_group.reset_index()

data_group.plot.area(x='month',y='Humidity', alpha=0.6)

plt.plot(data['Temperature (C)'])
plt.ylabel('Temperature (C)')
plt.xlabel('Reading number over time')
plt.show()