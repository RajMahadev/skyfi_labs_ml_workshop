##Importing Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt #For plotting

from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn import metrics 
from sklearn.model_selection import GridSearchCV #for parameter tuning

##Importing KNN
from sklearn.neighbors import KNeighborsClassifier 

## Get the cleaned data from data_cleaning.py where X, y are split into training and validation sets

### Model training
knn = KNeighborsClassifier(n_neighbors = 3) #Define the model
knn.fit(X_train, y_train) #Fit the model
train_accuracy_knn = round(knn.score(X_train, y_train) * 100, 2) #Training accuracy rounded to two numbers after decimal
validation_accuracy_knn = round(knn.score(X_val, y_val) * 100, 2) #Validation accuracy rounded to two numbers after decimal
print(train_accuracy_knn)
print(validation_accuracy_knn)

#Cross-Validation
cv_knn = cross_val_score(knn, X, y, cv=10, scoring='accuracy') #10-fold cross validation
print(f'Average accuracy is {cv_knn.mean()}') #Mean of 10 different values of accuracy

#Hyperparameter Optimization
parameter_grid_knn = {'n_neighbors': list(range(1,10))} #number of neighbors
gs_knn = GridSearchCV(knn,scoring='accuracy',param_grid=parameter_grid_knn, cv=10) #Searching through grid of parameters and noting the accuracies
gs_knn.fit(X,y) #Fit to the entire training data
parameters_knn = gs_knn.best_params_ #Store the best set of parameters for future use
print('Best score: {}'.format(gs_knn.best_score_)) #Print out the best accuracy
print('Best parameters: {}'.format(gs_knn.best_params_)) # Print out the best set of parameters