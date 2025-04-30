"""Question-27
 HandsOn - Titanic survival prediction , from Kaggle
https://www.kaggle.com/c/titanic/data
           
Understand data, download only train.csv and test.csv 

Using Tpot, find the test score of best Estimator 
Hint:
The first and most important step in using TPOT on any data set 
is to rename the target class/response variable to 'class'.

At present, TPOT requires all the data to be in numerical format. 
Categorical:  Name, Sex, Ticket, Cabin and Embarked.
So convert categorical to number(which preprocessing?) and/or 
discard high levels of categorical completely 

Keras:
data/pima-indians-diabetes.csv, Binary classification """


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tpot import TPOTClassifier

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train['Age'].fillna(train['Age'].median(), inplace=True)
train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)
train['Fare'].fillna(train['Fare'].median(), inplace=True)


le = LabelEncoder()
for col in ['Sex', 'Embarked']:
    train[col] = le.fit_transform(train[col])


train = train.drop(columns=['Name', 'Cabin', 'Ticket', 'PassengerId'])


train = train.rename(columns={'Survived': 'class'})


X = train.drop(columns='class')
y = train['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42)
tpot.fit(X_train, y_train)
print("Test Score:", tpot.score(X_test, y_test))


