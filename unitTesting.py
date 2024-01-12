def creating_the_graphs(data, graph_type='stacked_area', countries=None):
    
    #Create complex and informative graphs based on the data which i have cleansed. 
    #Here all of the possible outcomes for all the graphs which i have created. 

    #Parameters:
    # - data: DataFrame, the input data containing 'Entity', 'Year', 'Total food expenditure per year', and 'Prevalence of undernourishment (%)'.
    # - graph_type: str, the type of graph to create. Options: 'linear graph (food/undernourishment)', 'heatmap (food/undernourishment)' , 'grouped_bar (food/undernourishment)', 'bubble_chart'.
    # - countries: list, a list of country names to include in the graph (applies to 'grouped_bar' graph_type).
    # - returns the different types of graphs which i have made using the data. 
