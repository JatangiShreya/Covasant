"""
tpot/keras
Question-26
 HandsOn - Predict The Data Scientists Salary In India from kaggle use sklearn
dataset: Predict-The-Data-Scientists-Salary-In-India_Train_Dataset.csv
Data Features:
    Name of the company (Encoded)
    Years of experience(split to min and max experience)
    Job description
    Job designation
    Job Type
    Key skills
    Location (needs LabelEncoded)
    Salary in Rupees Lakhs(To be predicted)(needs LabelEncoded)
    
Find the best estimator among below 
clf1 = DecisionTreeClassifier()
clf2 = RandomForestClassifier(n_estimators=100)
clf3 = ExtraTreesClassifier(n_estimators=100)
clf4 =  AdaBoostClassifier(n_estimators=100)
clf5 =  GradientBoostingClassifier(n_estimators=100)"""



import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier

df = pd.read_csv("Predict-The-Data-Scientists-Salary-In-India_Train_Dataset.csv")

le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])
df['Salary'] = le.fit_transform(df['Salary'])


df[['MinExp', 'MaxExp']] = df['Years of experience'].str.extract(r'(\d+)\s*-\s*(\d+)').astype(float)


df = df.drop(columns=['Job description', 'Job designation', 'Key skills', 'Job Type'])

df = df.dropna()

X = df.drop(columns=['Salary', 'Years of experience'])
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf1 = DecisionTreeClassifier()
clf2 = RandomForestClassifier(n_estimators=100)
clf3 = ExtraTreesClassifier(n_estimators=100)
clf4 = AdaBoostClassifier(n_estimators=100)
clf5 = GradientBoostingClassifier(n_estimators=100)

clfs = [clf1, clf2, clf3, clf4, clf5]
names = ['DecisionTree', 'RandomForest', 'ExtraTrees', 'AdaBoost', 'GradientBoosting']


for name, clf in zip(names, clfs):
    score = cross_val_score(clf, X_train, y_train, cv=5).mean()
    print(f"{name}: Cross-Val Accuracy = {score:.4f}")

