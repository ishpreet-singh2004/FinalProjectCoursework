import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

#Code to display and call data which I am analysing (csv file).
pd.options.display.max_rows = 400

data = pd.read_csv('vscode final project data CSV.csv')
# print(data)

def creating_the_graphs(data, graph_type='stacked_area', countries=None):
    
    #Creating graphs based on the data which i have cleansed. 

    #Parameters:
    # - data: DataFrame, the input data containing 'Entity', 'Year', 'Total food expenditure per year', and 'Deaths by malnutrition per 100000 people'.
    # - graph_type: str, the type of graph to create. Options: 'linear graph (Food/Deaths by malnutrition)', 'heatmap (Food/Deaths by malnutrition)' , 'grouped_bar (Food/Deaths by malnutrition)', 'bubble_chart'.
    # - countries: list, a list of country names to include in the graph (applies to 'grouped_bar' graph_type).
    # - returns the different types of graphs which i have made using the data. 

    if graph_type == 'line_graph_food':
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

            # Show the plot (in this case return as its a function)
            return plt.gcf()

    elif graph_type == 'line_graph_undernourishment':
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

            # Show the plot (in this case return as its a function)
            return plt.gcf()
    
    elif graph_type == 'heatmap_food':
        # Pivot the data for heatmap
        heatmap_data = data.pivot(index='Entity', columns='Year', values=['Total food expenditure per year'])

        # Plotting heatmap
        plt.figure(figsize=(24, 24))
        sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
        plt.title('Heatmap of Food Expenditure Across Years and Countries')
        plt.xlabel('Year')
        plt.ylabel('Entity')
        # returning the graph
        return plt.gcf()
    
    elif graph_type == 'heatmap_undernourishment':
        # Pivot the data for heatmap
        heatmap_data = data.pivot(index='Entity', columns='Year', values=['Deaths by malnutrition per 100000 people'])

        # Plotting heatmap
        plt.figure(figsize=(24, 24))
        sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
        plt.title('Heatmap of Deaths by malnutrition Across Years and Countries')
        plt.xlabel('Year')
        plt.ylabel('Entity')
        # returinig the graph
        return plt.gcf()

    elif graph_type == 'grouped_bar_food':
        # Plotting grouped bar chart
        plt.figure(figsize=(30,12))
        sns.barplot(x='Entity', y='Total food expenditure per year', hue='Year', data=data)
        plt.title('Grouped Bar Chart of Food Expenditure and Undernourishment by Country')
        plt.xlabel('Country')
        plt.ylabel('Values')
        plt.xticks(rotation=45, ha='right')
        return plt.gcf()
    
    elif graph_type == 'grouped_bar_undernourishment':
        # Plotting grouped bar chart
        plt.figure(figsize=(30, 12))
        sns.barplot(x='Entity', y='Deaths by malnutrition per 100000 people', hue='Year', data=data,)
        plt.title('Grouped Bar Chart of Food Expenditure and Deaths by malnutrition by Country')
        plt.xlabel('Country')
        plt.ylabel('Values')
        plt.xticks(rotation=45, ha='right')
        # returning the graph
        return plt.gcf()

    elif graph_type == 'bubble_graph':
        # Plotting bubble chart
        fig = px.scatter(data, x='Total food expenditure per year', y='Deaths by malnutrition per 100000 people', size='Total food expenditure per year', color='Entity', animation_frame='Year',
                         title='Bubble Chart of Food Expenditure vs Undernourishment Over Years',
                         labels={'Total food expenditure per year': 'Total Food Expenditure', 'Deaths by malnutrition per 100000 people': 'Deaths by malnutrition'})
        # returning the graph
        return plt.gcf()
    else:
        raise ValueError(f"Unsupported graph_type: {graph_type}")
