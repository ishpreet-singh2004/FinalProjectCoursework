import matplotlib.pyplot as plt
import pandas as pd

# Assuming your data is in a DataFrame named 'df'
# Replace 'df' with the actual variable name if it's different.

# List of unique countries in the dataset
countries = data['Entity'].unique()

# Create a separate plot for each country
for country in countries:
    # Filter data for the specific country
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
