import plotly as py
import plotly.graph_objs as go
import numpy as np
import os

buttons2remove = '["toImage","sendDataToCloud","zoom2d","select2d","lasso2d","autoScale2d","resetScale2d"]'

layout = go.Layout(title = "An amazing interactive scatter plot",
                   xaxis = {"title": "A wonderful x-axis"})
trace_1 = go.Scatter(x = np.linspace(0,100,100),y = np.random.randn(100),name = "This one scatter plot",
                     mode = "markers"
                     )
trace_2 = go.Scatter(x = np.linspace(0,100,100),y = np.random.randn(100) + 5,name = "This is another scatter plot",
                     mode = "makers+lines"
                     )

my_path = "C:\\Users\joseg\Desktop\my-h4xx3d-plot.html" #You have to change this to your own path!

py.offline.plot({
    "data": [trace_1,
             trace_2],
    "layout": layout},
                filename = my_path,
    auto_open = False)

with open(my_path) as o:
    plot_ly = o.read()
    plot_ly = plot_ly.replace(', {"linkText": "Export to plot.ly", "showLink": true}','')
    plot_ly = plot_ly.replace('displaylogo:!0','displaylogo:!1')
    plot_ly = plot_ly.replace('modeBarButtonsToRemove:[]','modeBarButtonsToRemove:' + buttons2remove)
    #plot_ly = plot_ly.replace('displayModeBar:"hover"','displayModeBar:false')

with open(my_path,'w') as o:
    o.write(plot_ly)

print("Houston, we have a plot!")