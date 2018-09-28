import numpy as np 
import pandas as pd 


###Drop irrelevant details

train_data = train_data.drop(labels=['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1) 

#TODO- Do the same thing on test data


# check everything looks okay
print(train_data.head())


### Converting categorical variables

# Sex {male, female} to {0, 1}
train_data['Sex'] = train_data['Sex'].map( {'female': 1, 'male': 0} ).astype(int)

# Embarked {S, C, Q} => 3 binary variables
embarked_separate_port = pd.get_dummies(train_data['Embarked'], prefix='Embarked')
train_data = pd.concat([train_data, embarked_separate_port], axis=1)
train_data=train_data.drop('Embarked', axis=1)

#TODD- Convert categorical variables in test data in the same way

# Embarked {S, C, Q} => 3 binary variables

#Check if everything's okay
print(train_data.head())

###Filling Missing values-
#There are many ways to fill missing values and you can come up with a new way too.. there's no right or wrong way
# It's specific to the dataset 
# here's just an effective way to fill missing values of age with the mean of the age of the other people of that class and sex
guess_ages = np.zeros((2,3))

for i in range(0, 2):
	for j in range(0, 3):
		guess_data = train_data[(train_data['Sex'] == i) & (train_data['Pclass'] == j+1)]['Age'].dropna()
		age_guess = guess_data.median()

   		# Convert random age float to nearest .5 age
   		guess_ages[i,j] = int( age_guess/0.5 + 0.5 ) * 0.5

 
#For convenience, we define a function to call later for train and test data.
def wrangle_age(dataset):
	for i in range(0, 2):
		for j in range(0, 3):
			dataset.loc[(dataset.Age.isnull()) & (dataset.Sex == i) & (dataset.Pclass == j+1),'Age'] = guess_ages[i,j]
			dataset['Age'] = dataset['Age'].astype(int)

    return dataset

 
#Calling wrangle_age function on training and test data
train_data = wrangle_age(train_data)
test_data = wrangle_age(test_data)

##Converting SibSp and Parch to a new variable FamilySize
train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1
train_data=train_data.drop(['SibSp','Parch'],axis=1)

#TODO Create a similar variable in test data


