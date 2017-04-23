import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')     #https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

#Goals.txt file has 2 lines. Each line has a space between each number and end with a space + "\n" 
#First line belong to Home Team (HomeTeamGoals) and the second to Away Team
with open("Goals.txt","r") as f:
    HomeTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]  
    AwayTeamGoals = [int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

#Check "import matplotlib.pyplot as plt \n help(plt.plot)"
#plot() method creates a visual graphic.
#Note that you can provide only one argument to the plot() method
fig, ax = plt.subplots()
ax.plot(HomeTeamGoals)
ax.plot(AwayTeamGoals)
#Use legend() to specify each line
plt.show()

#If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you
#Lets compare!
fig, (ax1,ax2) = plt.subplots(2,1)         #We The subplot() command specifies numrows, numcols
xVariable = np.arange(len(HomeTeamGoals))  #length of HomeTeamGoals array
ax1.plot(xVariable, HomeTeamGoals)         #With X and Y argument
ax2.plot(HomeTeamGoals)                    #Without X argument
'''
set_title()
set_title()
suptitle()
'''
plt.show()

#Scatter() representa apenas os pontos do gráfico
#For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot
#Colors available: https://www.w3schools.com/cssref/css_colors.asp
fig, (ax1,ax2) = plt.subplots(2,1)
ax1.scatter(xVariable, AwayTeamGoals, c = "#FF1493", s = 12)
ax2.scatter(xVariable, HomeTeamGoals, c = "red", s = 12)
#Never forget to define the axis after you plot/scatter
ax2.set_xlim(60,80)                     #Edit X-axis. xlim(lower,upper)
ax2.set_ylim(-2,6)                      #Edit Y-axis. ylim(lower,upper)
plt.show()

#From now on lets just work with just one plot
#Check "import matplotlib.pyplot as plt \n help(plt.plot)"
fig, ax = plt.subplots()
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
fig, ax = plt.subplots()
ax.plot(HomeTeamGoals, ":g",label = 'HomeTeamGoal')
ax.set(ylim=(-0.2, 6),xlim=(-5, 150),xlabel=r'$\bigstar$Game Number$\bigstar$', ylabel='Goals Scored',title='Home Team first 50 games'); 
ax.set_yticks([0,1,2,3,4,5,6])
ax.set_yticklabels(['0 Goals','1 Goal','2 Goals', '3 Goals','4 Goals','5 Goals','6 Goals'], rotation = -45) 
ax.legend()
ax.text(np.random.randint(0,140),np.random.randint(0,6),'random place',fontsize = 20, color='red')
ax.annotate('local max', xy=(20, 6), xytext=(30,5.5),arrowprops=dict(facecolor='red', shrink=0.01))
plt.show() 





'''
#Exercise 1
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0, 10, 30)
y = np.sin(x)
ax.title('I Did it!')
ax.plot(x,y)               #Add the correct properties
ax.legend()                #Display the label on the correct position
ax.axis()                  #Define the axis
plt.show()
'''

'''
#Exercise 2
fig, ax = plt.subplots()
x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')
ax.title('I Did it again!')

ax.annotate('local maximum',
            #ArrowHead coord, 
            #Text Coord,
            #arrowprops=dict()
            )

ax.annotate('local minimum', 
            #ArrowHead coord, 
            #Text Coord,
            bbox=dict(boxstyle="round", fc ='w',ec="b"),
            #arrowprops=dict()
            )
plt.show()
'''





















'''
x = np.linspace(0, 10, 30)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('I Did it!')
ax.plot(x, y, '-p', color='gray',
         markersize=14, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2,
         label = 'Exercise 1')
ax.legend(loc = 4,frameon = True,shadow = True, borderpad = 0.8)
ax.axis([-0.2,10.2,-1.1, 1.1])
plt.show()


plt.title('I Did it!')
plt.plot(x, y, '-p', color='gray',
         markersize=14, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2,
         label = 'Exercise 1')
plt.legend(loc = 4,frameon = True,shadow = True, borderpad = 0.8)
plt.axis([-0.2,10.2,-1.1, 1.1])
plt.show()
'''


'''
fig, ax = plt.subplots()
x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('local maximum', xy=(2*np.pi, 1), xytext=(10, 4),
            arrowprops=dict(facecolor='black', shrink=0.05,width = 0.8))

ax.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
            bbox=dict(boxstyle="round", fc ='w',ec="b"),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="angle3,angleA=0,angleB=-90"));
plt.show()





plt.plot(x, np.cos(x))
plt.axis('equal')

plt.annotate('local maximum', xy=(2*np.pi, 1), xytext=(10, 4),
            arrowprops=dict(facecolor='black', shrink=0.05,width = 0.8))

plt.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
            bbox=dict(boxstyle="round", fc ='w',ec="b"),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="angle3,angleA=0,angleB=-90"));
plt.show()
'''