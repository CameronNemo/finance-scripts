import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bones.csv', parse_dates=['ts'], index_col='ts')
plt.plot(df.groupby('ts').sum().values)
plt.show()
