# -*- coding: utf-8 -*-
import pandas as pd

#Import the train.csv file
sydney_file_path = 

home_data =

#Step 1 - Specify the prediction target

#Select the target variable, which corresponds to the sales price. Save this to a new variable called `y`. You'll need to print a list of the columns to find the name of the column you need.



# print the list of columns in the dataset to find the name of the prediction target

y = 

#Step 2: Create X

#Now you will create a DataFrame called `X` holding the predictive features.

#Since you want only some columns from the original data, you'll first create a list with the names of the columns you want in `X`.
#
#You'll use just the following columns in the list (you can copy and paste the whole list to save some typing, though you'll still need to add quotes):
#    * LotArea
#    * YearBuilt
#    * 1stFlrSF
#    * 2ndFlrSF
#    * FullBath
#    * BedroomAbvGr
#    * TotRmsAbvGrd


#After you've created that list of features, use it to create the DataFrame that you'll use to fit the model.


## Create the list of features below

feature_names =  


# select data corresponding to features in feature_names

X = 


# Review data
# print description or statistics from X


# print the top few lines
print()


#Step 3: Specify and Fit Model
#Create a `DecisionTreeRegressor` and save it as home_model. Ensure you've done the relevant import from sklearn to run this command.


home_model = 

#Then fit the model you just created using the data in `X` and `y` that you saved above.

home_model.fit(X,y)

#Step 4: Make Predictions

predictions = 
print(predictions)



#Think About Your Results

#Use the `head` method to compare the top few predictions to the actual home values (in `y`) for those same homes. Anything surprising?

#You'll understand why this happened if you keep going.










