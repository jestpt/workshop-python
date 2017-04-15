#########################################################################
################ IV - WORKING WITH A DIFFERENT DATASET ##################
#########################################################################

#first, we are going to need a new module so let's start by importing it
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

#let's load this differente dataset I was talking about
digits = datasets.load_digits()

#and let's get a good look at it to spot the differences
print(digits.DESCR)

#let's see how our dataset is organized so we can better explore it latter
print(digits.images.shape)
print(digits.data.shape)

#let's explore one of this matrixes so we can better understand the situation
plt.imshow(digits.images[23], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

#########################################################################
################ V - UNDER AND OVER FITTING YOUR MODEL ##################
#########################################################################

#on my last chapter with you I want to talk about the risks of under e over fitting
#for this let's change our neighbors number between 1 and 9
neighbors =np.arange(1, 9)

#for this we'll plot a graph so let's store our data on
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

#as we did on Iris dataset let's create our X_train, X_test, y_train and y_test
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,
                                                    random_state = 10,
                                                    stratify = y)

#to generate the values 9 times let's loop over the various values of k
for i, k in enumerate(neighbors):
    #let's create a classifier with k neighbors
    knn = KNeighborsClassifier(n_neighbors = k)
    
    #let's do the fitting
    knn.fit(X_train, y_train)
    
    #Compute the accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)
    
    #Compute the accuracy on the test set
    test_accuracy[i] = knn.score(X_test, y_test)
    
#to end your time with me, unfortunatelly, let's plot our final graph and take some conclusions
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()