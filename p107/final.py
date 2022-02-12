# Processing the data 
import pandas as pd
#To read data values in the data file 
import csv
#To draw the graph 
import plotly.graph_objects as go

#Read the values and store in varible df
df = pd.read_csv("data.csv")

# Assigning the address value to each data value in the data file, loc = location 
student_df = df.loc[df['student_id'] == "TRL_987"]

#To caltculate the mean and to print the values of it in the terminal. 
print(student_df.groupby("level")["attempt"].mean())

#To plot the graph with x and y values with orientation = horizontal (h) 
fig = go.Figure(go.Bar(
            x=student_df.groupby("level") ["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level4' ],
            orientation='h'))
#Displaying the graph 
fig.show()
