import plotly as py
import plotly.graph_objs as go

py.offline.plot({
    "data": [go.Scatter(x = [1,2,34,5,6],y = [1,45,64,4,2])],
    "layout": go.Layout(title = "An amazing interactive scatter plot",
                        xaxis = {"title": "A wonderful x-axis"})},
    filename = "C:\Users\joseg\Desktop\my-scatter-plot.html") #You have to change this to your own path!

print("Houston, we have a plot!")