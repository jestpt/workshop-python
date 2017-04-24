import plotly as py
import plotly.graph_objs as go
import numpy as np

my_path = "C:\\Users\joseg\Desktop\my-lots-of-things.html" #You have to change this to your own path!

x1 = ["oranges","peaches","bananas","apples","pears","pineapples","grapefruits","cucumber"]
y1 = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
z1 = [np.random.randint(0,50,len(x1)) for i in y1]
z2 = [np.random.randint(0,50,len(x1)) for i in y1] #This time we will be creating two different z values

#This is how I make buttons! It is really confusing, a bunch of lists/dictionaries nested in lists/dictionaries...
#This is the general "architecture" of buttons, so if we want to add more buttons we just need to create a new
#dictionary inside the "buttons" list. "restyle" changes the layout options
updatemenus=list([
    dict(type = "buttons",
        buttons=list([   
            dict(
                args=['type', 'heatmap'],
                label='heatmap',
                method='restyle'
            ),
            dict(
                args=['type', 'surface'],
                label='3d surface',
                method='restyle'
            )
            ]),
        y = -0.1,
        x = 0.5,
        direction = 'left',        
        ),
    dict(type = "buttons",
         buttons = list([
            dict(
                args = [{'visible': [True,False]},
                        {'title':'Consumo de fruta do Jose'}],
                label='Jose',
                method='update'
            ),
            dict(
                args=[{'visible': [False,True]},
                      {'title':'Consumo de fruta do Bruno'}],
                label='Bruno',
                method='update'
            )            
            ]),
         y = 0.5,
         x = -0.1
        )
    ])


trace_1 = go.Heatmap(x = x1,
                     y = y1,
                     z = z1
                     )

trace_2 = go.Heatmap(x = x1,
                     y = y1,
                     z = z2,
                     visible = False
                     )

layout = go.Layout(title = "Consumo de fruta do Jose",
                   updatemenus = updatemenus)

py.offline.plot({
    "data": [trace_1,
             trace_2],
    "layout":layout},
                filename = my_path,
    auto_open = False)

print("Houston, we have a plot!")