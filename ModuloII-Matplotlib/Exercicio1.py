import matplotlib.pyplot as plt
import numpy as np

#Goals.txt file has 2 lines. Each line has a space between each number and end with a space + "\n" 
#First line belong to Home Team (HomeTeamGoals) and the second to Away Team
with open("Goals.txt","r") as f:
    HomeTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]  
    AwayTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

#Check "import matplotlib.pyplot as plt \n help(plt.plot)"
#plot() method creates a visual graphic.
#Note that you can provide only one argument to the plot() method
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(HomeTeamGoals)
ax.plot(AwayTeamGoals)
plt.show()

#If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you
#Lets compare!
fig, (ax1,ax2) = plt.subplots(2,1)                           #We The subplot() command specifies numrows, numcols, fignum where fignum ranges from 1 to numrows*numcols
xVariable = np.arange(len(HomeTeamGoals))  #length of HomeTeamGoals array
ax1.plot(xVariable, HomeTeamGoals)         #With X and Y argument
ax2.plot(HomeTeamGoals)                    #Without X argument
plt.show()

#Scatter() representa apenas os pontos do gráfico
#For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot
#Colors available: https://www.w3schools.com/cssref/css_colors.asp
fig, (ax1,ax2) = plt.subplots(2,1)
ax1.scatter(xVariable, AwayTeamGoals, c = "#FF1493", s = 12)
ax2.scatter(xVariable, HomeTeamGoals, c = "red", s = 12)
ax2.set_xlim(60,80)                     #Edit X-axis. xlim(lower,upper)
ax2.set_ylim(-2,6)                      #Edit Y-axis. ylim(lower,upper)
plt.show()

#From now on lets just work with just one plot
#Check "import matplotlib.pyplot as plt \n help(plt.plot)"
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("Home Team first 50 games")        #Adds a title to the plot
ax.plot(xVariable, HomeTeamGoals, "g^-")
ax.set_xlabel(r'$\bigstar$Game Number$\bigstar$')  #Adds a label on X-axis. This label uses latex syntax to reoresent special symbols
#To see more about latex special symbols check:
#http://artofproblemsolving.com/wiki/index.php?title=LaTeX:Symbols
#https://www.codecogs.com/latex/eqneditor.php                 <--------This is for the lazy ones
ax.set_ylabel('Goals Scored')                      #Adds a lable on Y-axis.
ticks = ['0 Goals','1 Goal','2 Goals', '3 Goals','4 Goals','5 Goals','6 Goals']
plt.yticks([0,1,2,3,4,5,6],ticks)               #The labels in the 'ticks' array will be written on the corresponding position
ax.set_ylim(bottom=-1)
ax.set_xlim(0,50)
#Try seting xlim and ylim in one code line!
#Note: use axis() method
plt.show()

#Now lets try to simplify the code
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(HomeTeamGoals, ":g",label = 'HomeTeamGoal')
ax.set(ylim=(-0.2, 6),xlim=(-5, 150),xlabel=r'$\bigstar$Game Number$\bigstar$', ylabel='Goals Scored',title='Home Team first 50 games'); 
plt.yticks([0,1,2,3,4,5,6],['0 Goals','1 Goal','2 Goals', '3 Goals','4 Goals','5 Goals','6 Goals'], rotation = -45) 
ax.legend()
ax.text(np.random.randint(0,140),np.random.randint(0,6),'random place',fontsize = 20, color='red')
ax.annotate('local max', xy=(20, 6), xytext=(30,5.5),arrowprops=dict(facecolor='red', shrink=0.01),)
plt.show()
