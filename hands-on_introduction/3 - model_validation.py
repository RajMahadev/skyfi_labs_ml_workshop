import pandas as pd

melbourne_file_path = './melbourne_housing_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

melbourne_data.dropna(axis=0)

y = melbourne_data.Price

melbourne_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']

X = melbourne_data[melbourne_features]

X.describe()

X.head(n=10)

from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor(random_state=1)

#Fit model
melbourne_model.fit(X,y)

#Make predictions for first five rows
#print(X.head())

#Predictions
#print(melbourne_model.predict(X.head()))


#What is Model Validation

#You'll want to evaluate almost every model you ever build. In most (though not all) applications, the relevant measure of model quality is predictive accuracy. In other words, will the model's predictions be close to what actually happens.
#
#Many people make a huge mistake when measuring predictive accuracy. They make predictions with their training data and compare those predictions to the target values in the training data. You'll see the problem with this approach and how to solve it in a moment, but let's think about how we'd do this first.
#
#You'd first need to summarize the model quality into an understandable way. If you compare predicted and actual home values for 10,000 houses, you'll likely find mix of good and bad predictions. Looking through a list of 10,000 predicted and actual values would be pointless. We need to summarize this into a single metric.
#
#There are many metrics for summarizing model quality, but we'll start with one called Mean Absolute Error (also called MAE). Let's break down this metric starting with the last word, error.

from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)

mean_absolute_error(y,predicted_home_prices)


#The Problem with "In-Sample" Scores

#The measure we just computed can be called an "in-sample" score. We used a single "sample" of houses for both building the model and evaluating it. Here's why this is bad.
#
#Imagine that, in the large real estate market, door color is unrelated to home price.
#
#However, in the sample of data you used to build the model, all homes with green doors were very expensive. The model's job is to find patterns that predict home prices, so it will see this pattern, and it will always predict high prices for homes with green doors.
#
#Since this pattern was derived from the training data, the model will appear accurate in the training data.
#
#But if this pattern doesn't hold when the model sees new data, the model would be very inaccurate when used in practice.
#
#Since models' practical value come from making predictions on new data, we measure performance on data that wasn't used to build the model. The most straightforward way to do this is to exclude some data from the model-building process, and then use those to test the model's accuracy on data it hasn't seen before. This data is called validation data.

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.

train_X,test_X,train_y,test_y = train_test_split(X,y,random_state=0)

#Define the model

melbourne_model = DecisionTreeRegressor()

#Fit the model

melbourne_model.fit(train_X,train_y)

# get predicted prices on validation data
test_predictions = melbourne_model.predict(test_X)

mean_absolute_error(test_y,test_predictions)


















