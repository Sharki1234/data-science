import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

wine_data = pd.read_csv("wine.csv")

fig1 = px.scatter(wine_data,x = "alcohol",y = "density",size = "sulphates",color = "quality")
#fig1.write_html("Fig1.html",auto_open = True)

fig2 = px.histogram(wine_data,x = "alcohol",y = "quality",color= "quality")
#fig2.write_html("Fig2.html",auto_open = True)

fig3 = go.Figure(data=[
    go.Scatter(name = "Scatter",x = wine_data["alcohol"],y = wine_data["density"],mode = "markers",marker = dict(size = wine_data["sulphates"]*10,color = wine_data["quality"])),
    go.Histogram(name = "Histogram",x = wine_data["alcohol"])
])

fig3.write_html("Fig3.html",auto_open = True)

figure = make_subplots(rows = 1,cols = 2,subplot_titles="alcohol distrubution,alcohol vs density",horizontal_spacing=0.1)
figure.add_trace(go.Scatter(name = "Scatter",x = wine_data["alcohol"],y = wine_data["density"],mode = "markers",marker = dict(size = wine_data["sulphates"]*10,color = wine_data["quality"])),
                 row =1,col=2)
figure.add_trace(row = 1,col=1,trace = go.Histogram(name = "Histogram",x = wine_data["alcohol"]))
figure.write_html("figure.html",auto_open = True)