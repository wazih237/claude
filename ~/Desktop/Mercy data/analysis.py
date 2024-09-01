import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('clean_monkey_pox.csv')

# Group by Age group, Sex, and Province, and count Final_Classification
grouped_data = data.groupby(['Age group', 'Sex', 'Province'])['Final_Classification'].count().reset_index()

# Create a pivot table to show 'Age group', 'Sex' and group by 'Province'
province_pivot = data.pivot_table(index=['Province', 'Age group', 'Sex'], values='Final_Classification', aggfunc='count')
print(province_pivot)

import matplotlib.pyplot as plt
import seaborn as sns

# Create a table
print(province_pivot)

# Create a graph for each unique feature in 'Province'
provinces = data['Province'].unique()
for province in provinces:
    province_data = data[data['Province'] == province]
    pivot_province = province_data.pivot_table(index=['Age group', 'Sex'], values='Final_Classification', aggfunc='count')
    print(f"Table for {province}:")
    print(pivot_province)
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Age group', y='Final_Classification', hue='Sex', data=pivot_province.reset_index())
    plt.title(f"Final Classification by Age group and Sex for {province}")
    plt.tight_layout()
    plt.savefig(f"{province}_bar_chart.png")
    plt.show()
import pandas as pd

# Load the data
data = pd.read_csv('clean_monkey_pox.csv')

# Filter data for 'Positif' in 'Test_Result'
positif_data = data[data['Test_Result'] == 'Positif']

# Group by 'Province' and count
positif_province_counts = positif_data.groupby('Province').size().reset_index(name='Count')

# Sort by 'Count' in descending order
positif_province_counts = positif_province_counts.sort_values('Count', ascending=False)

# Print the table
print(positif_province_counts)
