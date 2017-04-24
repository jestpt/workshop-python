import plotly as py
import plotly.graph_objs as go
import numpy as np

my_path = "C:\\Users\joseg\Desktop\my-box-plot.html" #You have to change this to your own path!

#Define my labels and my random data
y1 = [1,45,40,41,42,43,44.4,43.2,46.8,62,6,8,10,22,45,40,43,36,46,47.8,50.3,75]

#Get our traces. Introducing Box and its parameters!
#Very simple boxplot
trace_1 = go.Box(y = y1,
                 #boxmean = False,
                 boxpoints = False,
                 name = "esto es una caja")

#Simple boxplot paired with dotplot
trace_2 = go.Box(y = y1,
                 #boxmean = True,
                 boxpoints = "all",
                 name = "isto e uma caixa")

#Default boxplot showing outliers
trace_3 = go.Box(y = y1,
                 #boxmean = "sd",
                 boxpoints = "outliers",
                 marker = dict(color = 'rgb(107,174,214)'),
                 name = "this is a box")

#What about boxmean????

py.offline.plot({
    "data": [trace_1,
             trace_2,
             trace_3]},
    filename = my_path,
    auto_open = False)

print("Houston, we have a plot!")