import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

with open("Goals.txt","r") as f:
    HomeTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.hist(x = HomeTeamGoals,
        bins = range(8),
        label = "Home Team Goals",
        align = "left")
ax.legend()
ax.set_xlabel("Goals Scored")
ax.set_ylabel("Games Played")
plt.show()


TotalGoals = HomeTeamGoals + AwayTeamGoals
fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111)
ax.hist(x = (HomeTeamGoals,AwayTeamGoals,TotalGoals),
         bins = range(8),
         label = ["Home Team Goals","Away Team Goals", 
         "Total Goals Scored"],
         align = "left"
         )
ax.legend()
ax.set_xlabel("Goals Scored")
ax.set_ylabel("Games Played")
plt.show()



fig, ax = plt.subplots()
#divider = make_axes_locatable(ax)
#cax = divider.append_axes( 'bottom',size='5%', pad=0.55)
H = ax.hist2d(x = HomeTeamGoals,
           y = AwayTeamGoals,
           bins = (range(8),range(7)))
ax.set_xlabel("Home Team Goals")
ax.set_ylabel("Away Team Goals")

print(H[3])
print('------------------------------------------------------------------')
print(H)

bar = fig.colorbar(H[3],orientation='horizontal')
bar.set_label('Goals')
plt.show()
