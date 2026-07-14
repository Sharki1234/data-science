import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\rakhi\Downloads\WHO-COVID-19-global-data (1).csv")
data["DateReported"] = pd.to_datetime(data["DateReported"])
data_england = data[data["Country"]=="The United Kingdom"]
#print(data_england.head())
x = data_england["New_cases"]
x2 = data_england["New_deaths"]
y = data_england["DateReported"]

plt.plot(y,x)
plt.plot(y,x2)
plt.show()

#uber times
uber_data = pd.read_csv(r"C:\Users\rakhi\AppData\Local\Temp\a129fb02-9d19-47bb-99b1-007a041c37d2_archive.zip.7d2\other-American_B01362.csv")
uber_data["DATE"] = pd.to_datetime(uber_data["DATE"])
date_data= uber_data["DATE"].value_counts().fillna(0)

date_data.plot(kind = "line",xlabel="dates",ylabel="no_of each")
plt.show()