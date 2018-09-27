## Recap
#You've built a model. In this exercise you will test how good your model is.

#Exercises


## Step 1: Split Your Data
#Use the `train_test_split` function to split up your data.
#
#Give it the argument `random_state=1` so the `check` functions know what to expect when verifying your code.
#
#Recall, your features are loaded in the DataFrame **X** and your target is loaded in **y**.

# Import the train_test_split function
from _ import _

train_X, val_X, train_y, val_y = _


## Step 2: Specify and Fit the Model

#Create a `DecisionTreeRegressor` model and fit it to the relevant data.
#Set `random_state` to 1 again when creating the model.


# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again

# Specify the model
sydney_model = _

# Fit sydney_model with the training data.
_


## Step 3: Make Predictions with Validation data

# Predict with all validation observations
val_predictions = _


#Inspect your predictions and actual values from validation data.


# print the top few validation predictions
print(_)
# print the top few actual prices from validation data
print(_)


#What do you notice that is different from what you saw with in-sample predictions (which are printed after the top code cell in this page).
#
#Do you remember why validation predictions differ from in-sample (or training) predictions? This is an important idea from the last lesson.


## Step 4: Calculate the Mean Absolute Error in Validation Data

from sklearn.metrics import mean_absolute_error
val_mae = _


#Is that MAE good?  There isn't a general rule for what values are good that applies across applications. But you'll see how to use this number in the next step.




