from sys import displayhook
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

#Code to display and call data which I am analysing (csv file).

pd.options.display.max_rows = 400

data = pd.read_csv('vscode final project data CSV.csv')
displayhook(data)
