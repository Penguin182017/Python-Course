import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = {
    'Age': [2, 5, 4, 6, 7],
    'Weight': [3.4, 5, 6, 4.5, 5.2],
    'Height': [13, 14, 31, 23, 34]
}

df = pd.DataFrame(df)

sns.pairplot(df)

plt.show()