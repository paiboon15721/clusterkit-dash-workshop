import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

df = pd.read_csv('./salaries.csv')
df = df.sort_values('Salary', ascending=False)
df = df[df['Age'] > 30]

data = [go.Bar(x=df['Name'], y=df['Salary'])]

layout = go.Layout(title='Salary by Name', xaxis=dict(
    title='Name'), yaxis=dict(title='Salary'))

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
