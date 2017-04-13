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

#secondly, we import the sample datasets from skl to work
from sklearn import datasets

#for now let's work with the iris dataset
iris = datasets.load_iris()

#let's look at our dataset
print(iris)

#with pandas, let's work this a bit more so it's more presentable
iris_data = pd.DataFrame(datasets.load_iris().data)
iris_target = pd.DataFrame(datasets.load_iris().target)

#now we name the header of the columns with the information we have
iris_data.columns = ['sepal_lenght', 'sepal_width', 'petal_lenght', 'petal_width']
iris_target.columns = ['species']
print(iris_data.head())
print(iris_target.head())

#now let's start building our machine learning model !!!!
from sklearn.neighbors import KNeighborsClassifier

#after import we create the classifier as we like
knn = KNeighborsClassifier(n_neighbors = 6)

#now we are going to feed our classifier X aka the features and y aka the classes
X = iris_data.values
y = iris_target.values

#to end it we fit our classifier to our data
knn.fit(X, y)

#now, although it's not correct, let's test our model against the dataset we used to create it
print(knn.score(X, y))

#########################################################################
########## II - TRAIN / TEST SPLIT + FIT / PREDICT / ACCURACY ###########
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