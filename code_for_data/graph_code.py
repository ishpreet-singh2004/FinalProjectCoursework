#graph 1 
import matplotlib.pyplot as plt
import pandas as pd

# List of unique countries in the dataset
countries = data['Entity'].unique()

# Create a separate plot for each country
for country in countries:
    # Filter data for the specific country
    country_data = data[data['Entity'] == country]

    # Plotting for food prices
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


#graph 2 
import matplotlib.pyplot as plt
import pandas as pd

# List of unique countries in the dataset
countries = data['Entity'].unique()

# Create a separate plot for each country
for country in countries:
    # Filter data for the specific country
    country_data = data[data['Entity'] == country]

    # Plotting for nourishment
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['Deaths by malnutrition per 100000 people'], label='Undernourishment')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(f'{country} - Undernourishment Over the Years')

    # Adding legend
    plt.legend()

    # Show the plot
    plt.show()

#graph 3 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Pivot the data for heatmap
heatmap_data = data.pivot(index='Entity', columns='Year', values=['Total food expenditure per year'])

# Plotting heatmap for food expenditure
plt.figure(figsize=(24, 24))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
plt.title('Heatmap of Food Expenditure Across Years and Countries')
plt.xlabel('Year')
plt.ylabel('Entity')
plt.show()

#graph 4 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Pivot the data for heatmap
heatmap_data = data.pivot(index='Entity', columns='Year', values=['Deaths by malnutrition per 100000 people'])

# Plotting heatmap for undernourishment
plt.figure(figsize=(24, 24))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
plt.title('Heatmap of Undernourishment Across Years and Countries')
plt.xlabel('Year')
plt.ylabel('Entity')
plt.show()

#graph 5 
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting grouped bar chart for food expenditure 
plt.figure(figsize=(30,12))
sns.barplot(x='Entity', y='Total food expenditure per year', hue='Year', data=data)
plt.title('Grouped Bar Chart of Food Expenditure and Undernourishment by Country')
plt.xlabel('Country')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')
plt.show()

#graph 6 
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting grouped bar chart for undernourishment
plt.figure(figsize=(30, 12))
sns.barplot(x='Entity', y='Deaths by malnutrition per 100000 people', hue='Year', data=data,)
plt.title('Grouped Bar Chart of Food Expenditure and Undernourishment by Country')
plt.xlabel('Country')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')
plt.show()

#graph 7 
import plotly.express as px

# Plotting bubble chart for both variables being compared to each other
fig = px.scatter(data, x='Total food expenditure per year', y='Deaths by malnutrition per 100000 people', size='Total food expenditure per year', color='Entity', animation_frame='Year',
                 title='Bubble Chart of Food Expenditure vs Undernourishment Over Years',
                 labels={'Total food expenditure per year': 'Total Food Expenditure', 'Deaths by malnutrition per 100000 people': 'Undernourishment'})
fig.show()