#Import pandas library
import pandas as pd

#Store the path to the dataset in a variable
dataset = '../datasets/melbourne_housing_data.csv'

#Import the dataset
melbourne_data = pd.read_csv(dataset)

#Statistical description of data
description = melbourne_data.describe()


