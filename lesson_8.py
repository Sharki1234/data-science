import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv(r"C:\Users\rakhi\Downloads\WHO-COVID-19-global-data (1).csv")

data["DateReported"] = pd.to_datetime(data["DateReported"])

data_dates = data.groupby("DateReported").sum()

figure = go.Figure()
figure.add_trace(go.Scatter(x = data_dates.index,y = data_dates["Cumulative_cases"],line_color="blue"))
#figure.show()

figure2 = go.Figure()
figure2.add_trace(go.Scatter(x = data_dates.index,y = data_dates["New_cases"]))
#figure2.show()

data_France = data[(data["Country"]=="France")]
figure3 = go.Figure()
figure3.add_trace(go.Scatter(x = data_France["DateReported"],y = data_France["New_cases"]))
#figure3.show()

data_England = data[(data["Country"]=="England")]
figure4 = go.Figure()
figure4.add_trace(go.scatter.Line(x = data_England["DateReported"],y =  data_England["New_cases"]))
figure4.add_trace(go.scatter.Line(x = data_England["DateReported"],y =  data_England["New_deaths"]))
figure4.show()