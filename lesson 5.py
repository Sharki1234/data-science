<<<<<<< HEAD
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#getting dataset
dataset = pd.read_csv(r"C:\Users\rakhi\Downloads\Data (1).csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#filling in missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#encoding independant variables
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder= "passthrough")
x = np.array(ct.fit_transform(x))
print(x)#makes France and Spain and GErmany into binary patters like 0,0,1 or 1,0,0

#encoding dependant variables
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

=======
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#getting dataset
dataset = pd.read_csv(r"C:\Users\rakhi\Downloads\Data (1).csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#filling in missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#encoding independant variables
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder= "passthrough")
x = np.array(ct.fit_transform(x))
print(x)#makes France and Spain and GErmany into binary patters like 0,0,1 or 1,0,0

#encoding dependant variables
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

>>>>>>> 2a100f3d6b6ce1bf2454eb7243359b48ae24c89c
