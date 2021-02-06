import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px
df = pd.read_csv('data4.csv')
#studentdf = df.loc[df['student_id'] == 'TRL_abc']
mean = df.groupby(['student_id','level'],as_index = False)['attempt'].mean()
print (mean)
fig = px.scatter(mean, x = 'student_id', y = 'level', size = 'attempt', color = 'attempt')
fig.show()
