from sys import displayhook
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px

import unittest
from unitTesting import creating_the_graphs

data = pd.read_csv('vscode final project data CSV.csv')

class testingFunction(unittest.TestCase):

    def test_stacked_area_chart(self):
        # Test stacked area chart creation
        chart = creating_the_graphs(data, graph_type='line_graph_food')
        self.assertIsInstance(chart, plt.Figure)

    def test_grouped_bar_chart(self):
        # Test grouped bar chart creation
        chart = creating_the_graphs(data, graph_type='line_graph_undernourishment')
        self.assertIsInstance(chart, plt.Figure)
    
    def test_stacked_area_chart(self):
        # Test stacked area chart creation
        chart = creating_the_graphs(data, graph_type='heatmap_food')
        self.assertIsInstance(chart, plt.Figure)

    def test_grouped_bar_chart(self):
        # Test grouped bar chart creation
        chart = creating_the_graphs(data, graph_type='heatmap_undernourishment')
        self.assertIsInstance(chart, plt.Figure)

    def test_grouped_bar_chart(self):
        # Test grouped bar chart creation
        chart = creating_the_graphs(data, graph_type='grouped_bar_food')
        self.assertIsInstance(chart, plt.Figure)

    def test_grouped_bar_chart(self):
        # Test grouped bar chart creation
        chart = creating_the_graphs(data, graph_type='grouped_bar_undernourishment')
        self.assertIsInstance(chart, plt.Figure)

    def test_bubble_chart(self):
        # Test bubble chart creation
        chart = creating_the_graphs(data, graph_type='bubble_graph')
        self.assertIsInstance(chart, type(px.scatter()))

    def test_invalid_chart_type(self):
        # Test invalid chart type
        with self.assertRaises(ValueError):
            creating_the_graphs(data, graph_type='invalid_chart_type')

if __name__ == '__main__':
    unittest.main()