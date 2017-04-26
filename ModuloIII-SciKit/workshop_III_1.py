#########################################################################
########## JEST - Junior Enterprise for Science and Technology ##########
#########################################################################
############# data_science.py - Python for Machine Learners #############
#########################################################################

#########################################################################
############## I - WORK AROUND AND K-NEAREST NEIGHBORS FIT ##############
#########################################################################

## --- first, we import the packages we are going to use

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import sklearn as skl
from sklearn import datasets

## --- for now let's work with the iris dataset

iris = datasets.load_iris()

## --- let's look at our dataset

print('# --- How is our data stored?')
print(type(iris))

print('# --- What are the keys of this dictionary?')
print(iris.keys())

print('# --- What is the data?')
print(iris['feature_names'])
print(iris['data'])
print('Ammount of data: ', len(iris['data']))

print('# --- What is the target?')
print(iris['target_names'])
print(iris['target'])
print('Ammount of targets: ' + str(len(iris['data'])))

## --- so let's separate our data from our target

X = iris['data']
y = iris['target']

## --- now we'll use pandas to name the columns and have a nice look at our
##   features

iris_table = pd.DataFrame(X, columns = iris['feature_names'])
print('# --- Better visualization with Pandas')
print(iris_table.head())

## --- to do some cool visual EDA we'll use seaborn that we already imported as
##   sns

iris_EDA = sns.load_dataset("iris")
sns.pairplot(iris_EDA, hue='species')
sns.plt.show()

## --- now let's start building our machine learning model !!!!

from sklearn.neighbors import KNeighborsClassifier

### --- after import we create the classifier as we like. To avoid draws, it is
##   recommended that the number of neighbors selected is not multiple of:
##      x, being x in the set of {2, 3, 4, ... n_classes}
##      In this case we have three classes, so n_neighbors should not be
##      multiple of 2 or 3 (n_classes = 3)
##      Therefore, n_neighbors could be: 5, 7, 11, ...

knn = KNeighborsClassifier(n_neighbors = 15)

## --- using X and y defined previously we'll fit our dataset to the classifier
##   we just created

knn.fit(X, y)

## --- but what is fitting our data to the classifier?

X_2 = iris.data[:, :2] ## --- We'll only work with the first 2 features
h = .02
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
for weights in ['uniform', 'distance']:
    clf = KNeighborsClassifier(15, weights=weights)
    clf.fit(X_2, y)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (15, weights))

plt.show()

## --- now, although it's not correct, let's test our model against the dataset
##   we used to create it

print(knn.score(X, y))

#########################################################################
############### II - TRAIN / TEST SPLIT + FIT / ACCURACY ################
#########################################################################

## --- for this we'll need some more modules so let's get them

from sklearn.model_selection import train_test_split

## --- we already have our data and target defined but, as I said, it's not good
##   practice to score the classifier against the dataset we used to train it so
##   let's use a new method to make our model more accurate and open world ready

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 42,
                                                    stratify = y)

## --- once again, let's fit our data to the classifier

knn.fit(X_train, y_train)

## --- and to conclude this part let's see how this works

print(knn.score(X_test, y_test))

#########################################################################
############## III - PREDICT (WITHOUT KNOWING THE TRUTH) ################
#########################################################################

## --- now, we are going to use predict() to see how we can use our classifier
##   on new, unidentified samples for example, we have new data X

X_new = [5.7, 3.8, 1.7, 0.3]

## --- we already trained and fitted our classifier so let's put it to use

new_prediction = knn.predict(X_new)

print('Classified as: ', iris['target_names'][new_prediction])

## --- So, with an accuracy of 0.966666666667 we can say it's a Iris Setosa

#########################################################################
################ IV - WORKING WITH A DIFFERENT DATASET ##################
#########################################################################

## --- let's load this differente dataset I was talking about

digits = datasets.load_digits()

## --- and let's get a good look at it to spot the differences

print(digits.DESCR)

## --- let's see how our dataset is organized so we can better explore it later

print(digits.images.shape)
print(digits.data.shape)

## --- let's explore one of this matrixes so we can better understand the
##   situation

plt.imshow(digits.images[23], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

#########################################################################
##################### V - OVERFITTING YOUR MODEL ########################
#########################################################################

## --- on my last chapter with you I want to talk about the risks of overfitting
##   for this let's change our neighbors number between 1 and 9

neighbors =np.arange(1, 10)

## --- for this we'll plot a graph so let's store our data on

train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

## --- as we did on Iris dataset let's use train_test_split function

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,
                                                    random_state = 10,
                                                    stratify = y)

## --- to generate the values 9 times let's loop over the various values of k
for i, k in enumerate(neighbors):
    ## --- let's create a classifier with k neighbors
    knn = KNeighborsClassifier(n_neighbors = k)

    ## --- let's do the fitting
    knn.fit(X_train, y_train)

    ## --- Compute the accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    ## --- Compute the accuracy on the test set
    test_accuracy[i] = knn.score(X_test, y_test)

## --- to end your time with me, unfortunatelly, let's plot our final graph and
##   take some conclusions

plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()

#########################################################################
############### VI - ANOTHER THING - CROSS VALIDATION ###################
#########################################################################

## --- Despite separating train/test sets there's a risk that the knowledge
##   about test set can "leak" into the model and evaluation metrics no longer
##   report on generalization performance. So, one solution could be using 
##   a validation set but diving our dataset in three isn't good practice. So
##   let's use cross-validation (CV for short).

from sklearn import cross_validation

X = digits.data
y = digits.target

knn = KNeighborsClassifier(n_neighbors = 15)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y,
                                                    test_size=0.1,
                                                    random_state=10)

## --- first let's see the values without cross validation

knn.fit(X_train, y_train)

knn.score(X_train, y_train)

knn.score(X_test, y_test)

## --- now let's see how it goes with cross validation

for i in range(0,10):
    X_train_cv_train,X_test_cv_train, y_train_cv_train, y_test_cv_train = cross_validation.train_test_split(X_train, y_train, test_size=0.2/0.9)
    
    knn.fit(X_train_cv_train, y_train_cv_train)

knn.score(X_train, y_train)

knn.score(X_test, y_test)

#########################################################################
################# VII - TO FINISH - CONFUSION MATRIX ####################
#########################################################################

import itertools
from sklearn.metrics import confusion_matrix

## ---  import some data to play with
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

## ---  Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

## --- Run classifier

knn = KNeighborsClassifier(n_neighbors = 15)
y_pred = knn.fit(X_train, y_train).predict(X_test)


def plot_confusion_matrix(cm, classes,
                          normalize=True,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

## --- Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

print(cnf_matrix)

## --- Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()