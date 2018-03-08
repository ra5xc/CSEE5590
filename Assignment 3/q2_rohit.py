# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:05:34 2018

@author: rabhishe
"""

# Support Vector Machine (SVM)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split #importing the library for training and testing of the data
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap

# Import the datasets for social network ads
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values #Column 2,3 for age and estimated salary
y = dataset.iloc[:, 4].values #feature dataset



X_training, X_testing, y_training, y_testing = train_test_split(X, y, test_size = 0.4, random_state = 0) #Traiining set and Testing set

#Feature Scaling so that smaller numeric values are not dominted by the greater ones
scaling = StandardScaler()
X_training = scaling.fit_transform(X_training) #Scaling the training data
X_testing = scaling.transform(X_testing) #Scaling the testing data

# Applying Support Vector to the Training set

clf1 = SVC(kernel = 'linear', random_state = 0) #Applying linear kernel
clf2 = SVC(kernel = 'rbf', random_state = 0) #Applying RBF kernel
clf1.fit(X_training, y_training)
clf2.fit(X_training, y_training)

# Test Result prediction
y_predict1 = clf1.predict(X_testing)
y_predict2 = clf2.predict(X_testing)



# Plot the Training set for linear kernel

set_X, set_y = X_training, y_training
X1, X2 = np.meshgrid(np.arange(start = set_X[:, 0].min() - 1, stop = set_X[:, 0].max() + 1, step = 0.01),
                     np.arange(start = set_X[:, 1].min() - 1, stop = set_X[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, clf1.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.3, cmap = ListedColormap(('blue', 'yellow')))
print ("Accuracy Score for Training set for Linear Kernel is")
print (clf1.score(set_X, set_y))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for k, l in enumerate(np.unique(set_y)):
    plt.scatter(set_X[set_y == l, 0], set_X[set_y == l, 1],
                c = ListedColormap(('blue', 'yellow'))(k), label = l)
plt.title('Linear Kernel:Training set')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Plot the Testing set for linear kernel

set_X, set_y = X_testing, y_testing
X1, X2 = np.meshgrid(np.arange(start = set_X[:, 0].min() - 1, stop = set_X[:, 0].max() + 1, step = 0.01),
                     np.arange(start = set_X[:, 1].min() - 1, stop = set_X[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, clf1.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.3, cmap = ListedColormap(('blue', 'yellow')))
print ("Accuracy Score for Testing set for Linear Kernel is")
print (clf1.score(set_X, set_y))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for k, l in enumerate(np.unique(set_y)):
    plt.scatter(set_X[set_y == l, 0], set_X[set_y == l, 1],
                c = ListedColormap(('blue', 'yellow'))(k), label = l)
plt.title('Linear Kernel:Testing set')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()





# Plot the Training set for RBF kernel

set_X, set_y = X_training, y_training
X1, X2 = np.meshgrid(np.arange(start = set_X[:, 0].min() - 1, stop = set_X[:, 0].max() + 1, step = 0.01),
                     np.arange(start = set_X[:, 1].min() - 1, stop = set_X[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, clf2.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.3, cmap = ListedColormap(('blue', 'yellow')))
print ("Accuracy Score for Training set for RBF Kernel is")
print (clf2.score(set_X, set_y))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for k, l in enumerate(np.unique(set_y)):
    plt.scatter(set_X[set_y == l, 0], set_X[set_y == l, 1],
                c = ListedColormap(('blue', 'yellow'))(k), label = l)
plt.title('RBF Kernel:Training set')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Plot the Testing set for RBF kernel

set_X, set_y = X_testing, y_testing
X1, X2 = np.meshgrid(np.arange(start = set_X[:, 0].min() - 1, stop = set_X[:, 0].max() + 1, step = 0.01),
                     np.arange(start = set_X[:, 1].min() - 1, stop = set_X[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, clf2.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.3, cmap = ListedColormap(('blue', 'yellow')))
print ("Accuracy Score for Testing set for RBF Kernel is")
print (clf2.score(set_X, set_y))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for k, l in enumerate(np.unique(set_y)):
    plt.scatter(set_X[set_y == l, 0], set_X[set_y == l, 1],
                c = ListedColormap(('blue', 'yellow'))(k), label = l)
plt.title('RBF Kernel:Testing set')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()





