import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('clean_monkey_pox.csv')

# Group by Age group, Sex, and Province, and count Final_Classification
grouped_data = data.groupby(['Age group', 'Sex', 'Province'])['Final_Classification'].count().reset_index()

# Create a pivot table
pivot_table = grouped_data.pivot_table(index=['Age group', 'Sex'], columns='Province', values='Final_Classification', aggfunc='sum')

# Create a heatmap
plt.figure(figsize=(10, 8))
plt.imshow(pivot_table, cmap='hot', interpolation='nearest')
plt.xlabel('Province')
plt.ylabel('Age group and Sex')
plt.title('Final Classification by Age group, Sex, and Province')
plt.show()
