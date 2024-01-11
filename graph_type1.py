#Graph 1

# List of unique countries in the dataset
countries = data['Entity'].unique()

# Create a separate plot for each country
for country in countries:
    # Filter data for the specific country
    countries_data = data[data['Entity'] == country]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(countries_data['Year'], countries_data['Total food expenditure per year'], label='Food Expenditure')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(f'{country} - Food Expenditure Over the Years')

    # Adding legend
    plt.legend()

    # Show the plot
    plt.show()



