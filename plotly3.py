import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('./salaries.csv')
sr = df['Role'].value_counts()

data = [go.Pie(labels=sr.index, values=sr.values)]

layout = go.Layout(title='total employees by role')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)