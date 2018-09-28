##Importing Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt #For plotting

from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn import metrics 
from sklearn.model_selection import GridSearchCV #for parameter tuning

##Importing Random Forests
from sklearn.ensemble import RandomForestClassifier 

## Get the cleaned data from data_cleaning.py where X, y are split into training and validation sets

### Model training

#Define the model
random_forest = RandomForestClassifier(n_estimators=100)

#Step 1: Fit the model and print the training and validation accuracies

#Step 2: Do 10 fold cross-validation and print the mean_accuracy

#Step 3: Tune the parameters
#Step 3a: Define the dictionary of the parameter grid

#Step 3b: Do GridSearch and find the best set of parameters