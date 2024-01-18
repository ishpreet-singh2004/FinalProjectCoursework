import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

#Code to display and call data which I am analysing (csv file).
##
pd.options.display.max_rows = 400

data = pd.read_csv('vscode final project data CSV.csv')
# print(data)

def creating_the_graphs(data, graph_type='stacked_area', countries=None):
    
    #Create complex and informative graphs based on the data which i have cleansed. 
    #Here all of the possible outcomes for all the graphs which i have created. 

    #Parameters:
    # - data: DataFrame, the input data containing 'Entity', 'Year', 'Total food expenditure per year', and 'Prevalence of undernourishment (%)'.
    # - graph_type: str, the type of graph to create. Options: 'linear graph (food/undernourishment)', 'heatmap (food/undernourishment)' , 'grouped_bar (food/undernourishment)', 'bubble_chart'.
    # - countries: list, a list of country names to include in the graph (applies to 'grouped_bar' graph_type).
    # - returns the different types of graphs which i have made using the data. 

    if graph_type == 'line_graph_food':
        # Stacked Area Chart
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
            return plt.gcf()

    elif graph_type == 'line_graph_undernourishment':
        # Grouped Bar Chart
        # List of unique countries in the dataset
        countries = data['Entity'].unique()

        # Create a separate plot for each country
        for country in countries:
            # Filter data for the specific country
            country_data = data[data['Entity'] == country]

            # Plotting
            plt.figure(figsize=(10, 6))
            plt.plot(country_data['Year'], country_data['Prevalence of undernourishment (%)'], label='Undernourishment')

            # Adding labels and title
            plt.xlabel('Year')
            plt.ylabel('Value')
            plt.title(f'{country} - Undernourishment Over the Years')

            # Adding legend
            plt.legend()

            # Show the plot
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
        return plt.gcf()
    
    elif graph_type == 'heatmap_undernourishment':
        # Pivot the data for heatmap
        heatmap_data = data.pivot(index='Entity', columns='Year', values=['Prevalence of undernourishment (%)'])

        # Plotting heatmap
        plt.figure(figsize=(24, 24))
        sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=.5)
        plt.title('Heatmap of Undernourishment Across Years and Countries')
        plt.xlabel('Year')
        plt.ylabel('Entity')
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
        sns.barplot(x='Entity', y='Prevalence of undernourishment (%)', hue='Year', data=data,)
        plt.title('Grouped Bar Chart of Food Expenditure and Undernourishment by Country')
        plt.xlabel('Country')
        plt.ylabel('Values')
        plt.xticks(rotation=45, ha='right')
        return plt.gcf()

    elif graph_type == 'bubble_graph':
        # Plotting bubble chart
        fig = px.scatter(data, x='Total food expenditure per year', y='Prevalence of undernourishment (%)', size='Total food expenditure per year', color='Entity', animation_frame='Year',
                         title='Bubble Chart of Food Expenditure vs Undernourishment Over Years',
                         labels={'Total food expenditure per year': 'Total Food Expenditure', 'Prevalence of undernourishment (%)': 'Undernourishment'})
        fig.show()
        return plt.gcf()
    else:
        raise ValueError(f"Unsupported graph_type: {graph_type}")

#here im going to run the tests 