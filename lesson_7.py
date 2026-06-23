import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv(r"C:\Users\rakhi\Downloads\covid_data.csv")

data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]#collects only that
data.columns = ("State","Country","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active")#renames columns

data["State"].fillna(value="",inplace=True)


top10 = pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
fig1 = px.scatter(top10,x = top10.index,y = "Confirmed",size = "Confirmed",size_max = 120,color = top10.index,title = "Top 10")
fig1.write_html("Fig1.html",auto_open = True)

top10d = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False))
fig2 = px.bar(top10d,x = top10d.index,y="Deaths",color = top10.index,title = "Top 10")
fig2.write_html("Fig2.html",auto_open = True)

top_us = data["Country"] == "US"
top_us = data[top_us].nlargest(10,"Confirmed")
top_japan = data["Country"] == "Japan"
top_japan = data[top_japan].nlargest(10,"Confirmed")
print(top_us.head())

fig3 = go.Figure(data=[
    go.Bar(name = "Confirmed cases",x = top_us["Confirmed"],y = top_us["State"],orientation="h"),
    go.Bar(name = "Confirmed cases",y = top_japan["State"],x = top_japan["Confirmed"],orientation="h")
])
fig3.write_html("Fig3.html",auto_open = True)
