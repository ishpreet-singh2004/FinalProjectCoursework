import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
import plotly
import plotly.express as px

# importing unittest module to help carry out the tests 
import unittest
# calling the function being used from the specifc file name
from testing_function import creating_the_graphs

# the data the tests will be using 
data = pd.read_csv('vscode final project data CSV.csv')

class TestingFunction(unittest.TestCase):

    def test_stacked_area_chart_food(self):
        # Test for linear graph creation for food
        chart = creating_the_graphs(data, graph_type='line_graph_food')
        self.assertIsInstance(chart, plt.Figure)

    def test_stacked_area_chart_undernourishment(self):
        # Test for linear graph creation for deaths by malnutrition 
        chart = creating_the_graphs(data, graph_type='line_graph_deaths_by_malnutrition')
        self.assertIsInstance(chart, plt.Figure)

    def test_heatmap_chart_food(self):
        # Test for heatmap chart creation for food
        chart = creating_the_graphs(data, graph_type='heatmap_food')
        self.assertIsInstance(chart, plt.Figure)

    def test_heatmap_chart_undernourishment(self):
        # Test for heatmap chart creation for deaths by malnutrition 
        chart = creating_the_graphs(data, graph_type='heatmap_deaths_by_malnutrition')
        self.assertIsInstance(chart, plt.Figure)

    def test_grouped_bar_chart_food(self):
        # Test for grouped bar chart creation for food
        chart = creating_the_graphs(data, graph_type='grouped_bar_food')
        self.assertIsInstance(chart, plt.Figure)

    def test_grouped_bar_chart_undernourishment(self):
        # Test for grouped bar chart creation for deaths by malnutrition 
        chart = creating_the_graphs(data, graph_type='grouped_bar_deaths_by_malnutrition')
        self.assertIsInstance(chart, plt.Figure)
    
    def test_bubble_chart(self):
        # Test for bubble chart creation
        chart = creating_the_graphs(data, graph_type='bubble_graph')
        # Adjust this based on the actual return type of px.scatter()
        self.assertIsInstance(chart, plt.Figure)

    def test_invalid_chart_type(self):
        # Test for invalid chart type
        with self.assertRaises(ValueError):
            creating_the_graphs(data, graph_type='invalid_chart_type')

if __name__ == '__main__':
    unittest.main()
