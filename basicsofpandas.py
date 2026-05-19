import pandas as pd
# series = pd.Series([1,3,5,7],index=["a","b","c","d"])#series is a 1 dimensional array that holds all data types
# print(series["a"])#access an item by index
# print(series)
# #basically the indexes are like the dictionary keys

# my_dict = {
#     "car": 4,
#     "truck":4,
#     "bike":2
# }

# series2 = pd.Series(my_dict)
# print(series2["car"])#see Output:4

# series3 = pd.Series(my_dict,index = ["car","bike"])#makes a series with only car and bike
# print(series3)
# #__________________________________________________________________________________________________________#
# #DATAFRAMES

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data,index = ["A","B","c"])#data frames are multi dimentional tables
# #while series is like a column data frames are tables
# #Output:
# #   calories  duration
# #A       420        50
# #B       380        40
# #c       390        45


# print (myvar.loc["A"])#prints row A
# print (myvar.loc[["A","B"]])#prints row A and B
# print(myvar)

# #reading csvs
# df = pd.read_csv('data.csv')
# #you can open file by doing f = open("data.csv","x")

# print(df.to_string()) 
# #output without .to_string()
# #      Duration  Pulse  Maxpulse  Calories
# # 0          60    110       130     409.1
# # 1          60    117       145     479.0
# # 2          60    103       135     340.0
# # 3          45    109       175     282.4
# # 4          45    117       148     406.0
# # ..        ...    ...       ...       ...
# # 164        60    105       140     290.8
# # 165        60    110       145     300.0
# # 166        60    115       145     310.2
# # 167        75    120       150     320.4
# # 168        75    125       150     330.4

# #JSON objects have the same format as Python dictionaries.

# data = pd.DataFrame({
#     "Name":["Kim Dokja","Mitsuki Kado"],
#     "Age" : [27,17],
#     "City" :["Seoul","Tokyo"]

# },index=["ORV","TGW"])

# print(data.head())
# print(data.shape)
# print(data["Name"])
# print(data["Age"].max())
# print(data.info())
# print(data.describe())

# new_data = pd.DataFrame(data[["Age","Name"]])#makes new table with these two columns
# print(new_data.head())

# above20 = data[data["Age"]>20]#checks for age above 20
# print(above20.head())

titanic = pd.read_csv(r"C:\Users\rakhi\Downloads\titanic.csv")
# class1and3 = titanic[titanic["Pclass"].isin([1,3])]#check for whose class is 1 or 3
# onlyname = class1and3["Name"]
# print(class1and3.head())

# class2and1 = titanic[(titanic["Pclass"] == 1)| (titanic["Pclass"]==2)]#same as isin but without the function
# print(class2and1.head)

Malefirstclass = titanic[(titanic["Pclass"]==1)&(titanic["Sex"]=="male")]
print(Malefirstclass.head())
print(Malefirstclass["Fare"].mean())

Femalesecondclass = titanic[(titanic["Pclass"]==2)&(titanic["Sex"]=="female")]
print(Femalesecondclass.head())
print(Femalesecondclass["Fare"].mean())
