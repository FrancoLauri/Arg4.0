import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import DataFrame
penguin_df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

# Create a count plot of penguin species by island
plt.figure(figsize=(10, 6))
sns.countplot(data=penguin_df, x='island', hue='species', palette='Set2')
plt.title('Distribution of Penguin Species by Island')
plt.xlabel('Island')
plt.ylabel('Count')
plt.legend(title='Species', loc='upper right')
plt.tight_layout()
plt.show()