import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import dataframes

penguin_df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

print(penguin_df.dtypes)

average_body_mass_by_sex = penguin_df.groupby('sex')['body_mass_g'].mean()

# Plot the average body mass
plt.figure(figsize=(8, 5))
average_body_mass_by_sex.plot(kind='bar', color='lightcoral')
plt.title('Average Body Mass by Sex')
plt.xlabel('Sex')
plt.ylabel('Average Body Mass (g)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()