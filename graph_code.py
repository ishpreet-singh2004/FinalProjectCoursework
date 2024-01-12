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
    plt.plot(country_data['Year'], country_data['Prevalence of undernourishment (%)'], label='Undernourishment')

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

# Assuming your data is in a DataFrame named 'df'
# Replace 'df' with the actual variable name if it's different.

# Pivot the data for heatmap
heatmap_data = data.pivot(index='Entity', columns='Year', values=['Total food expenditure per year'])

# Plotting heatmap
plt.figure(figsize=(24, 24))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
plt.title('Heatmap of Food Expenditure Across Years and Countries')
plt.xlabel('Year')
plt.ylabel('Entity')
plt.show()