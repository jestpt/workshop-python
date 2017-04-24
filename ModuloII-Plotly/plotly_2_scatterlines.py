import plotly as py #This is essentially the plot creator
import plotly.graph_objs as go #This will "design" the plots and help us costumize them
import numpy as np #Generating data randomly for demonstration purposes

#Generate random data to plot
x = np.linspace(0,100,10)
y1 = np.random.randn(10) + 5
y2 = np.random.randn(10)
y3 = [i - 5 for i in y2]

#We first define the general layout... some nice plot and axis titles should suffice for now
layout = go.Layout(title = "An amazing interactive scatter plot",
                        xaxis = {"title": "A wonderful x-axis"},
                        yaxis = {"title": "Not so wonderful but also good y-axis"})

#Here we are creating out scatter/lineplots and understand how to use "mode", "width", and line = {"dash","shape","color"}
#mode? line, markers, text
#width?
#dash? dot, dash, dashdot
#shape? spline, vhv, hvh, vh, hv
trace_1 = go.Scatter(x = x,y = y1,
                     name = "This one scatter plot",
                     line = {"shape":"spline",
                             "dash":"dashdot",
                             "width":10},
                     mode = "line")
trace_2 = go.Scatter(x = x,y = y2,
                     name = "This is another scatter plot",
                     line = {"shape":"vhv",
                             "dash":"dash",
                             "color":("rgb(134,123,34)")}
                     )

trace_3 = go.Scatter(x = x,y = y3,
                     name = "This is yet another scatter plot"
                     #I want a thin, dotted, pink line!
                     )

#Where will I be storing my graphs? Under what name?
my_path = "C:\\Users\joseg\Desktop\my-triple-plot.html" #You have to change this to your own path!

py.offline.plot({
    "data": [trace_1,
             trace_2,
             trace_3],
    "layout": layout},
    filename = my_path,
    auto_open = False)

print("Houston, we have a plot!")