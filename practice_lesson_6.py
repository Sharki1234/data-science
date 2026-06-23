<<<<<<< HEAD
import pandas as pd
import matplotlib as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

iris = pd.read_csv(r"C:\Users\rakhi\Downloads\iris.csv")


y = iris["species"]
x = iris.drop("species",axis=1)#data w/out species
le = LabelEncoder()
y = le.fit_transform(iris["species"])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

model = DecisionTreeClassifier(max_depth=3,random_state=1)

model.fit(x_train,y_train)

predictions = model.predict(x_test)

=======
import pandas as pd
import matplotlib as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

iris = pd.read_csv(r"C:\Users\rakhi\Downloads\iris.csv")


y = iris["species"]
x = iris.drop("species",axis=1)#data w/out species
le = LabelEncoder()
y = le.fit_transform(iris["species"])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

model = DecisionTreeClassifier(max_depth=3,random_state=1)

model.fit(x_train,y_train)

predictions = model.predict(x_test)

>>>>>>> 2a100f3d6b6ce1bf2454eb7243359b48ae24c89c
print("Accuracy",metrics.accuracy_score(predictions,y_test))