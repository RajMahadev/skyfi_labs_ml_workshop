##Importing Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt #For plotting

from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn import metrics 
from sklearn.model_selection import GridSearchCV #for parameter tuning

##Importing Logistic Regression
from sklearn.linear_model import LogisticRegression

## Get the cleaned data from data_cleaning.py where X, y are split into training and validation sets

### Model training
logistic = LogisticRegression() #Define the model
logistic.fit(X_train, y_train) #Fit the model
train_accuracy_log = round(logistic.score(X_train, y_train) * 100, 2) #Training accuracy rounded to two numbers after decimal
validation_accuracy_log = round(logistic.score(X_val, y_val) * 100, 2) #Validation accuracy rounded to two numbers after decimal
print(train_accuracy_log)
print(validation_accuracy_log)

#Cross-Validation
cv_log = cross_val_score(logistic, X, y, cv=10, scoring='accuracy') #10-fold cross validation
print(f'Average accuracy is {cv_log.mean()}') #Mean of 10 different values of accuracy


#Hyperparameter Optimization
parameter_grid_log = {'C': np.arange(1e-05, 3, 0.1)} #C-Penalty
gs_log = GridSearchCV(logistic,scoring='accuracy',param_grid=parameter_grid_log, cv=10) #Searching through grid of parameters and noting the accuracies
gs_log.fit(X,y) #Fit to the entire training data
parameters_log = gs_log.best_params_ #Store the best set of parameters for future use
print('Best score: {}'.format(gs_log.best_score_)) #Print out the best accuracy
print('Best parameters: {}'.format(gs_log.best_params_)) # Print out the best set of parameters