# -*- coding: utf-8 -*-

#Your dataset had too many variables to wrap your head around, or even to print out nicely. How can you pare down this overwhelming amount of data to something you can understand?

#We'll start by picking a few variables using our intuition. Later courses will show you statistical techniques to automatically prioritize variables.

import pandas as pd

melbourne_file_path = '../datasets/melbourne_housing_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

#The melbourne data has missing values, we will be dropping rows with the missing values. Later we will learn to handle missing data
melbourne_data.dropna(axis=0)

#Store the prediction target in a variable 
#In this case the prediction target will be house prices
#Usually the convention is that the variable for the prediction target is y

y = melbourne_data.Price

#Choosing features

#The columns that are inputted into our model (and later used to make predictions) are called "features." In our case, those would be the columns used to determine the home price. Sometimes, you will use all columns except the target as features. Other times you'll be better off with fewer features.
#
#For now, we'll build a model with only a few features. Later on you'll see how to iterate and compare models built with different features.
#
#We select multiple features by providing a list of column names inside brackets. Each item in that list should be a string (with quotes).

melbourne_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']

#By convention, this data is called X.

X = melbourne_data[melbourne_features]

X.describe()

X.head(n=10)

#Building your Model

#You will use the scikit-learn library to create your models. When coding, this library is written as sklearn, as you will see in the sample code. Scikit-learn is easily the most popular library for modeling the types of data typically stored in DataFrames.

from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor(random_state=1)

#Fit model
melbourne_model.fit(X,y)

#Make predictions for first five rows
print(X.head())
#Predictions
print(melbourne_model.predict(X.head()))


