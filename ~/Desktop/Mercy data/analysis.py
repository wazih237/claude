import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('clean_monkey_pox.csv')

# Group by Age group, Sex, and Province, and count Final_Classification
grouped_data = data.groupby(['Age group', 'Sex', 'Province'])['Final_Classification'].count().reset_index()

# Create a pivot table
pivot_table = grouped_data.pivot_table(index=['Age group', 'Sex'], columns='Province', values='Final_Classification', aggfunc='sum')

# Create a heatmap
import seaborn as sns
import matplotlib.pyplot as plt

# ...

# Create a bar chart
plt.figure(figsize=(10, 8))
sns.barplot(x='Province', y='Final_Classification', hue='Sex', data=pivot_table.reset_index())
plt.xlabel('Province')
plt.ylabel('Count of Final Classification')
plt.title('Final Classification by Age group, Sex, and Province')
plt.show()
