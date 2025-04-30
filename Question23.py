"""Use 
sklearn.datasets.load_breast_cancer
And Yellowbrick
Show confusion matrix and ROCAUC 
using Logistic regression 


#https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
#check wdbc.data or check  breast_cancer.csv , but use load_breast_cancer() 
#Diagnosis (M = malignant,1, B = benign,0) 
1) ID number
2) Diagnosis (M = malignant, B = benign)
3-32)Ten real-valued features are computed for each cell nucleus:
a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g) concavity (severity of concave portions of the contour)
h) concave points (number of concave portions of the contour)
i) symmetry
j) fractal dimension ("coastline approximation" - 1)
"""
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from yellowbrick.classifier import ConfusionMatrix, ROCAUC


data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=10000)

cm_viz = ConfusionMatrix(model, classes=["Benign", "Malignant"])
cm_viz.fit(X_train, y_train)
cm_viz.score(X_test, y_test)
cm_viz.show()

roc_viz = ROCAUC(model)
roc_viz.fit(X_train, y_train)
roc_viz.score(X_test, y_test)
roc_viz.show()

"""B. Use data/breast_cancer.csv
Use LabelEncoder and MinMaxScalar and Use pipeline 
Then GridSearch on param_grid = dict(lr__C=[0.1, 1, 10])
using Logistic regression """

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split


df = pd.read_csv("data/breast_cancer.csv")

if 'id' in df.columns:
    df = df.drop(columns='id')


le = LabelEncoder()
df['diagnosis'] = le.fit_transform(df['diagnosis'])  # M=1, B=0

X = df.drop(columns='diagnosis')
y = df['diagnosis']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


pipeline = Pipeline([
    ('scaler', MinMaxScaler()),
    ('lr', LogisticRegression(max_iter=10000))
])


param_grid = dict(lr__C=[0.1, 1, 10])
grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)


print("Best Parameters:", grid.best_params_)
print("Train Accuracy:", grid.score(X_train, y_train))
print("Test Accuracy:", grid.score(X_test, y_test))


