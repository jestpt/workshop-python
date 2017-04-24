import plotly as py
import plotly.graph_objs as go
import numpy as np

my_path = "C:\\Users\joseg\Desktop\my-histogram.html" #You have to change this to your own path!

x1 = np.random.randint(0,20,100)
x2 = np.random.randint(0,20,100)

#Just some histograms! histnorm ("count","probability"),opacity,autobinx,xbins
trace_1 = go.Histogram(x = x1,
                       histnorm = "probability",
                       opacity = 0.75,
                       name = "one crazzzzzzzzzzzzy histogram")
trace_2 = go.Histogram(x = x2,
                       histnorm = "probability",
                       opacity = 0.75,
                       autobinx = False,
                       xbins = {"size":0.5,"start":0,"end":20},
                       name = "this another crazzzzzzzzy histogram",)

#barmode? overlay and stack
layout = go.Layout(barmode = "overlay",
                   title = "Look at these great histograms!")

py.offline.plot({
    "data": [trace_1,
             trace_2],
    "layout":layout},
    filename = my_path,
    auto_open = False)

print("Houston, we have a plot!")