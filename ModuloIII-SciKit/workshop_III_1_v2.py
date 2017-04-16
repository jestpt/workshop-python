#########################################################################
########## JEST - Junior Enterprise for Science and Technology ##########
#########################################################################
############# data_science.py - Python for Machine Learners #############
#########################################################################

#########################################################################
############## I - WORK AROUND AND K-NEAREST NEIGHBORS FIT ##############
#########################################################################


#first, we import the packages we are going to use
import sklearn as skl
import pandas as pd
import os
import sys
import matplotlib.pylab as plt

#secondly, we import the sample datasets from skl to work
from sklearn import datasets

#for now let's work with the iris dataset
iris = datasets.load_iris()

#let's look at our dataset
print('# --- How is our data stored?')
print(type(iris))
print(iris)
os.system('pause')
os.system('cls')
print('# --- What are the keys of this dictionary?')
print(iris.keys())
os.system('pause')
print('# --- What is the data?')
print(iris['feature_names'])
print(iris['data'])
print('Ammount of data: ' + str(len(iris['data'])))
os.system('pause')
print('# --- What is the target?')
print(iris['target_names'])
print(iris['target'])
print('Ammount of targets: ' + str(len(iris['data'])))
os.system('pause')
os.system('cls')

#with pandas, let's work this a bit more so it's more presentable
iris_data = pd.DataFrame(iris['data'])

#now we name the header of the columns with the information we have
iris_data.columns = iris['feature_names']
#add the column with the targets
iris_data['Name'] = iris['target']

print(iris_data.head())
os.system('pause')
os.system('cls')
## Future note: 0 - Iris Setosa, 1 - Iris Versicolour, 2 - Iris Virginica ##

#now let's start building our machine learning model !!!!
from sklearn.neighbors import KNeighborsClassifier

#after import we create the classifier as we like
#to avoid draws, it is recommended that the number of neighbors selected is not multiple of:
#		x, being x in the set of {2, ... n_classes}
#		In this case we have three classes, so n_neighbors should not be multiple of 2 or 3 (n_classes = 3)
#		Therefore, n_neighbors could be: 5, 7, 11, ...
knn = KNeighborsClassifier(n_neighbors = 5)

#now we are going to feed our classifier X aka the features and y aka the classes
X = iris_data.values[:,0:4]
y = iris['target']

#to end it we fit our classifier to our data 
#(Training Phase)
knn.fit(X, y)

#graph
print(knn.kneighbors_graph(X))
ax = iris_data[iris_data.Name == 0].plot.scatter(x=iris_data.columns[0], y=iris_data.columns[1], color='blue', label='1')
ax = iris_data[iris_data.Name == 1].plot.scatter(x=iris_data.columns[0], y=iris_data.columns[1], color='red', label='2', ax=ax)
iris_data[iris_data.Name == 2].plot.scatter(x=iris_data.columns[0], y=iris_data.columns[1], color='green', label='3', ax=ax)
plt.show()
os.system('pause')
os.system('cls')

#now, although it's not correct, let's test our model against the dataset we used to create it
#(Test phase)
print(knn.score(X, y))
os.system('pause')
os.system('cls')
#########################################################################
############### II - TRAIN / TEST SPLIT + FIT / ACCURACY ################
#########################################################################

#for this we'll need some more modules so let's get them
from sklearn.model_selection import train_test_split

#we already have our data and target defined but, as I said, that's not good practice so let's use a new
#method to make our model more accurate and open world ready

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 42,
                                                    stratify = y)

#we already created a classifier but let's make another with different n_neighbors
knn = KNeighborsClassifier(n_neighbors = 7)

#once again, let's fit our data to the classifier
knn.fit(X_train, y_train)

#and to conclude this part let's see how this works
print(knn.score(X_test, y_test))

#########################################################################
############## III - PREDICT (WITHOUT KNOWING THE TRUTH) ################
#########################################################################

#now, we are going to use predict() to see how we can use our classifier on new, unidentified samples
#for example, we have new data X

X_new = [5.7, 3.8, 1.7, 0.3]

#we already trained and fitted our classifier so let's put it to use

new_prediction = knn.predict(X_new)

print(iris['target_names'][new_prediction])

#So, with an accuracy of 0.966666666667 we can say it's a Iris Setosa
