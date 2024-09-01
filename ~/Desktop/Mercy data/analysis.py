import pandas as pd

# Filter data for 'Positif' in 'Test_Result' and 'Genital Rashes' == 'Oui'
positif_genital_rashes_data = positif_data[(positif_data['Genital Rashes'] == 'Oui')]

# Group by 'Province' and count
positif_genital_rashes_province_counts = positif_genital_rashes_data.groupby('Province').size().reset_index(name='Count')

# Print the table
print(positif_genital_rashes_province_counts)
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
positif_sexual_contact_data = data[(data['Sexual_contact_with_someone_with_skin_lesions/Mpox'] == 'Oui') & (data['Test_Result'] == 'Positif')]

# Group by 'Province' and count
positif_province_counts = positif_data.groupby('Province').size().reset_index(name='Count')

# Sort by 'Count' in descending order
positif_province_counts = positif_province_counts.sort_values('Count', ascending=False)

# Print the table
provinces = positif_data['Province'].unique()
for province in provinces:
    province_data = positif_data[positif_data['Province'] == province]
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Age group', y='Count', hue='Sex', data=province_data)
    plt.title(f"Positif cases by Age group and Sex for {province}")
    plt.tight_layout()
    plt.savefig(f"{province}_positif_bar_chart.png")
    plt.show()
import pandas as pd

# Load the data
data = pd.read_csv('clean_monkey_pox.csv')

# Filter data for 'Positif' in 'Test_Result'
positif_data = data[data['Test_Result'] == 'Positif']

# Filter data for 'Positif' in 'Test_Result' and 'Genital Rashes' == 'Oui'
positif_genital_rashes_data = positif_data[(positif_data['Genital Rashes'] == 'Oui')]

# Group by 'Province' and count
positif_genital_rashes_province_counts = positif_genital_rashes_data.groupby('Province').size().reset_index(name='Count')

# Print the table
print(positif_genital_rashes_province_counts)
hospitalization_positif_oui_count = data[(data['Hospitalization'] == 'Oui') & (data['Test_Result'] == 'Positif')].shape[0]
print(f"Number of 'Hospitalization'=='Oui' and 'Test_Result'=='Positif': {hospitalization_positif_oui_count}")
# Load the data
data = pd.read_csv('clean_monkey_pox.csv')

# Filter data for 'Positif' in 'Test_Result'
positif_data = data[data['Test_Result'] == 'Positif']
import pandas as pd

# Load the data
data = pd.read_csv('clean_monkey_pox.csv')

# Filter data for 'Positif' in 'Test_Result'
positif_data = data[data['Test_Result'] == 'Positif']
positif_data = data[data['Test_Result'] == 'Positif']
epidemiological_link_oui_data = data[(data['Epidemiological_link'] == 'Oui')]
epidemiological_link_oui_province_counts = epidemiological_link_oui_data.groupby('Province').size().reset_index(name='Count')
print(epidemiological_link_oui_province_counts)
positif_sexual_contact_province_counts = positif_sexual_contact_data.groupby('Province').size().reset_index(name='Count')
print(positif_sexual_contact_province_counts)
positif_data = data[data['Test_Result'] == 'Positif']
