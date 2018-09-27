import pandas as pd

melbourne_file_path = './melbourne_housing_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

melbourne_data.dropna(axis=0)

y = melbourne_data.Price

melbourne_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']

X = melbourne_data[melbourne_features]

X.describe()

X.head(n=10)

from sklearn.model_selection import train_test_split


train_X,test_X,train_y,test_y = train_test_split(X,y,random_state=0)

from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_absolute_error


def get_mae(max_leaf_nodes,train_X,test_X,train_y,test_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes,random_state = 0)
    model.fit(train_X,train_y)
    predictions = model.predict(test_X)
    mae = mean_absolute_error(test_y,predictions)
    return mae
    

#Now that you have a reliable way to measure model accuracy, you can experiment with alternative models and see which gives the best predictions. But what alternatives do you have for models?
#
#You can see in scikit-learn's documentation that the decision tree model has many options (more than you'll want or need for a long time). The most important options determine the tree's depth. 

#Example
    
#There are a few alternatives for controlling the tree depth, and many allow for some routes through the tree to have greater depth than other routes. But the max_leaf_nodes argument provides a very sensible way to control overfitting vs underfitting. The more leaves we allow the model to make, the more we move from the underfitting area in the above graph to the overfitting area.


#We can use a for-loop to compare the accuracy of models built with different values for max_leaf_nodes.

# compare MAE with differing values of max_leaf_nodes

for max_leaf_nodes in [5,50,500,5000]:
    my_mae = get_mae(max_leaf_nodes,train_X,test_X,train_y,test_y)
    print("Max Leaf Nodes: %d  \t\t Mean Absolute Error: %d" %(max_leaf_nodes,my_mae))


#Of the options listed, 500 is the optimal number of leaves.










