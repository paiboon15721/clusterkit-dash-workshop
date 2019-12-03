import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df = pd.read_csv('./salaries.csv')
df = df.groupby('Role').sum()

data = [go.Pie(labels=df.index, values=df['Salary'])]

fig = go.Figure(data=data)
pyo.plot(fig)
