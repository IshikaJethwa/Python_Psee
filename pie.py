import pandas as pd
import plotly.express as px
import kaleido

df = pd.read_csv('SubjectMarks.csv')
l = list(df['Subject'])
values = df['Marks']
names = df['Subject'].tolist()

fig = px.pie(df, values=values, names=names, title="Student Marks analysis")
fig.show()
fig.write_image("images/fig1.png")