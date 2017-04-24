import plotly as py
import plotly.graph_objs as go
import numpy as np

my_path = "C:\\Users\joseg\Desktop\my-heatmap.html" #You have to change this to your own path!

#When we are dealing with heatmaps we need to have 3 coordinates: the x and y axis which will act as "categories"
#and the z axis which will act as the values for each intersection of x and y categories.
#Considering such, there will have to be x*y values for our x coordinates!
#Some great examples include the EVmutation web platform
x1 = ["oranges","peaches","bananas","apples","pears","pineapples","grapefruits","cucumber"]
y1 = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
z1 = [np.random.randint(0,50,len(x1)) for i in y1] #this loop creates len(y1) lists of length len(x1) of random integral numbers
#text1 = [["yummi: " + str(z1[j][i]) for i in range(0,len(x1))] for j in range(0,len(y1))] #this loop creates text values

#SUPER easy. We just have to assign our x "categories", our y "categories" and our z values.
trace_1 = go.Heatmap(x = x1,
                     y = y1,
                     z = z1
                     #hoverinfo = "text",
                     #text = text1
                     )

layout = go.Layout(title = "You gotta love heatmaps!")

py.offline.plot({
    "data": [trace_1],
    "layout":layout},
                filename = my_path,
    auto_open = False)

print("Houston, we have a plot!")