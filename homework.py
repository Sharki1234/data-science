import pandas as pd
import matplotlib as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv(r"C:\Users\rakhi\Downloads\iris.csv")

def one(dropped,prev=data.drop("species",axis=1)):
    y = data["species"]
    x = prev.drop(dropped,axis=1)
   
    le = LabelEncoder()
    y = le.fit_transform(data["species"])

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

    model = DecisionTreeClassifier(max_depth=3,random_state=1)

    model.fit(x_train,y_train)

    predictions = model.predict(x_test)

    print("Accuracy",metrics.accuracy_score(predictions,y_test))
    


dropped = ["sepal_length","sepal_width","petal_length","petal_width"]
for i in range(4):
    one(dropped[i])

    




