import plotly as py
import plotly.graph_objs as go
import numpy as np

my_path = "C:\\Users\joseg\Desktop\my-bar-plot.html" #You have to change this to your own path!

#Define my labels and my random data
x = ["healthy","not so healthy","almost dead","dead"]
y1 = [abs(i) for i in np.random.randn(4)]
y2 = [abs(i) for i in np.random.randn(4)]

#A function that helps me create simple annotations
def annotation_creator(x_list,y_list):
    out_list = [{"x":xi,
                 "y":yi,
                 "text":str(yi),
                 "xanchor":"center",
                 "yanchor":"bottom",
                 "showarrow":False} for xi,yi in zip(x_list,y_list)]
    return out_list

#Same boring layout... or is it? Introducing barmode ("group" and "stack") and annotations!
#annotations? [{x = ?,y = ?, text = ?,xanchor = ?,yanchor = ?,showarrow = ?}]
layout = go.Layout(title = "An amazing interactive barplot",
                   xaxis = {"title": "A wonderful x-axis"},
                   yaxis = {"title": "Not so wonderful but also good y-axis"},
                   barmode = "group"
                   #annotations = annotation_creator(x,y1)                   
                   )

#Create my bar plot traces. Good so far, but what else? Error bars!
#error_y({type("constant","data","percent"),symmetric,value and valueminus,array and arrayminus})
trace_1 = go.Bar(x = x,
                 y = y1,
                 text = ["good","not so good","kind of bad","REALLY bad"],
                 #
                 name = "control")
trace_2 = go.Bar(x = x,
                 y = y2,
                 #
                 name = "treatment")

py.offline.plot({
    "data": [trace_1],
    "layout": layout},
    filename = my_path,
    auto_open = False)

print("Houston, we have a plot!")