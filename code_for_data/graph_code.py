import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

#Code to display and call data which I am analysing (csv file).
pd.options.display.max_rows = 400

data = pd.read_csv('vscode final project data CSV.csv')
# print(data)

# Line graph
# List of the countries in the dataset
countries = data['Entity'].unique()

# Creates a separate plot for each country
for country in countries:
    # Filters data for the specific country
    country_data = data[data['Entity'] == country]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['Total food expenditure per year'], label='Food Expenditure')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(f'{country} - Food Expenditure Over the Years')

    # Adding legend
    plt.legend()

    # Show the plot
    plt.show()
        
# Grouped Bar Chart
# List of the countries in the dataset
countries = data['Entity'].unique()

# Creates a separate plot for each country
for country in countries:
    # Filters data for the specific country
    country_data = data[data['Entity'] == country]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['Deaths by malnutrition per 100000 people'], label='Deaths by malnutrition')
        
    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(f'{country} - Deaths by malnutrition Over the Years')

    # Adding legend
    plt.legend()

    # Show the plot 
    plt.show()
    
# Pivot the data for heatmap
heatmap_data = data.pivot(index='Entity', columns='Year', values=['Total food expenditure per year'])

# Plotting heatmap
plt.figure(figsize=(24, 24))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
plt.title('Heatmap of Food Expenditure Across Years and Countries')
plt.xlabel('Year')
plt.ylabel('Entity')
# returning the graph
plt.show()
    
# Pivot the data for heatmap
heatmap_data = data.pivot(index='Entity', columns='Year', values=['Deaths by malnutrition per 100000 people'])

# Plotting heatmap
plt.figure(figsize=(24, 24))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
plt.title('Heatmap of Deaths by malnutrition Across Years and Countries')
plt.xlabel('Year')
plt.ylabel('Entity')
# returinig the graph
plt.show()

# Plotting grouped bar chart
plt.figure(figsize=(30,12))
sns.barplot(x='Entity', y='Total food expenditure per year', hue='Year', data=data)
plt.title('Grouped Bar Chart of Food Expenditure and Undernourishment by Country')
plt.xlabel('Country')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')
plt.show()

# Plotting grouped bar chart
plt.figure(figsize=(30, 12))
sns.barplot(x='Entity', y='Deaths by malnutrition per 100000 people', hue='Year', data=data,)
plt.title('Grouped Bar Chart of Food Expenditure and Deaths by malnutrition by Country')
plt.xlabel('Country')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')
# returning the graph
plt.show()
    
# Plotting bubble chart
fig = px.scatter(data, x='Total food expenditure per year', y='Deaths by malnutrition per 100000 people', size='Total food expenditure per year', color='Entity', animation_frame='Year',
                    title='Bubble Chart of Food Expenditure vs Undernourishment Over Years',
                    labels={'Total food expenditure per year': 'Total Food Expenditure', 'Deaths by malnutrition per 100000 people': 'Deaths by malnutrition'})
# returning the graph
plt.show()
