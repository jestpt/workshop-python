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
plt.plot(HomeTeamGoals)
plt.plot(AwayTeamGoals)
plt.show()

#If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you
#Lets compare!
plt.subplot(211)                           #We The subplot() command specifies numrows, numcols, fignum where fignum ranges from 1 to numrows*numcols
xVariable = np.arange(len(HomeTeamGoals))  #length of HomeTeamGoals array
plt.plot(xVariable, HomeTeamGoals)         #With X and Y argument
plt.subplot(212)
plt.plot(HomeTeamGoals)                    #Without X argument
plt.show()

#Scatter() representa apenas os pontos do gráfico
#For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot
plt.subplot(211) 
plt.scatter(xVariable, AwayTeamGoals, c = "green", s = 12)
plt.subplot(212) 
plt.scatter(xVariable, HomeTeamGoals, c = "red", s = 12)
plt.xlim(60,80)                     #The most basic way to adjust axis limits is to use the plt.xlim() and plt.ylim() methods
plt.ylim(-2,6)                      
plt.show()

#From now on lets just work with just one plot
#Check "import matplotlib.pyplot as plt \n help(plt.plot)"
plt.title("Home Team first 50 games")     #Adds a title to the plot
plt.plot(xVariable, HomeTeamGoals, "g^-")
plt.xlim(0,50)
plt.ylim(-0.5,6)
plt.xlabel(r'$\bigstar$Game Number$\bigstar$')  #Adds a label on X-axis. This label uses latex syntax to reoresent special symbols
#To see more about latex special symbols check:
#http://artofproblemsolving.com/wiki/index.php?title=LaTeX:Symbols
#https://www.codecogs.com/latex/eqneditor.php                 <--------This is for the lazy ones
plt.ylabel('Goals Scored')                      #Adds a lable on Y-axis.
ticks = ['0 Goals','1 Goal','2 Goals', '3 Goals','4 Goals','5 Goals','6 Goals']
plt.yticks([0,1,2,3,4,5,6],ticks)               #The labels in the 'ticks' array will be written on the corresponding position
plt.ylim(bottom=-1)
plt.xlim(0,50)
plt.show()


#Now lets try to simplify the code
plt.plot(HomeTeamGoals, ":g",label = 'HomeTeamGoal')
plt.ylim=(-0.2, 6)
plt.xlim=(-5, 150)
plt.xlabel=(r'$\bigstar$Game Number$\bigstar$')
plt.ylabel=('Goals Scored')
plt.title=('Home Team first 50 games')
plt.yticks([0,1,2,3,4,5,6],['0 Goals','1 Goal','2 Goals', '3 Goals','4 Goals','5 Goals','6 Goals'], rotation = -45) 
plt.text(np.random.randint(0,140),np.random.randint(0,6),'random place',fontsize = 20, color='red')
plt.annotate('local max', xy=(20, 6), xytext=(30,5.5),arrowprops=dict(facecolor='red', shrink=0.01))
plt.legend()
plt.show() 
