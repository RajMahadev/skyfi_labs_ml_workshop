import pandas as pd
import numpy as np
#For plotting
import matplotlib.pyplot as plt
import seaborn as sns


#Import data into variables
train_data = pd.read_csv('../datasets/titanic/train.csv')

#TODO - Import test file into test_data
test_data = 


#See what training data contains
print(train_data.head())
print(train_data.info())

#Statistical details of the data
print(train_data.describe())  # Gives information only about continuous variables

train_data.describe(include=['O'])  #Gives information about categorical variables

#Just another way to count the number of missing values in each column
print(train_data.isnull().sum())

###Visualization

##No. of people who survived and who failed
train_data.Survived.value_counts().plot(kind='bar')
plt.title("Distribution of Survival, (1 = Survived)")


##Check the impact of Age and Sex
g = sns.FacetGrid(train_data, col='Survived')
g.map(plt.hist, 'Age', bins=20)

#TODO- Similar to Age, check the imapact of Sex


##Effect of Passenger Class on Survival rate

#Distribution of people in classes
train_data.Pclass.value_counts().plot(kind="barh")
plt.title("Class Distribution")

#Survival rate in each class
pclass_survived = train_data[train_data['Survived']==1]['Pclass'].value_counts()
pclass_dead = train_data[train_data['Survived']==0]['Pclass'].value_counts()
df = pd.DataFrame([pclass_survived,pclass_dead])
df.index = ['Survived','Dead']
df.plot(kind='bar', stacked=True, figsize=(10,8))

#TO DO 
#Exercise: Do an analogous analysis on the port from where people embarked- 'Embarked' column

#Distribution of people across ports


#Survival rate based on ports


##Effect of fare on survival
survived_0 = train_data[train_data['Survived'] == 0]["Fare"].mean()
survived_1 = train_data[train_data['Survived'] == 1]["Fare"].mean()
xs  = [survived_0, survived_1]
ys = ['Dead','Survived']
plt.bar(ys, xs, 0.6, align='center',color = 'green')
plt.xlabel('Outcome')
plt.ylabel('Mean Fare')
plt.show()