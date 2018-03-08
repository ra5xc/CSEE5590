#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:33:04 2018

@author: rohitabhishek
"""
#LDA
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap


dataset=pd.read_csv('wine.csv')
X_set=dataset.iloc[:,0:13].values
y_set=dataset.iloc[:,13].values
X_training, X_testing,y_training,y_testing=train_test_split(X_set,y_set,test_size=0.2,random_state=0)


l=LDA(n_components=2) #2 dimensional
X_training=l.fit_transform(X_training,y_training)
X_testing=l.transform(X_testing)







#Applying Logistics Regression
clsf=LogisticRegression(random_state=0)
clsf.fit(X_training,y_training)


#Test Result prediction
y_predication=clsf.predict(X_testing)


# Plot the data- Training set

set_X, set_y = X_training, y_training
X1, X2 = np.meshgrid(np.arange(start = set_X[:, 0].min() - 1, stop = set_X[:, 0].max() + 1, step = 0.01),
                     np.arange(start = set_X[:, 1].min() - 1, stop = set_X[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, clsf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.3, cmap = ListedColormap(('blue', 'yellow')))
print ("Accuracy Score is")
print (clsf.score(set_X, set_y))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for k, l in enumerate(np.unique(set_y)):
    plt.scatter(set_X[set_y == l, 0], set_X[set_y == l, 1],
                c = ListedColormap(('blue', 'yellow'))(k), label = l)
plt.title('Training set')
plt.xlabel('Linear Discriminant 1')
plt.ylabel('Linear Discriminant 2')
#plt.legend()
#plt.show()



# Plot the data- Testing Set

set_X, set_y = X_testing, y_testing
X1, X2 = np.meshgrid(np.arange(start = set_X[:, 0].min() - 1, stop = set_X[:, 0].max() + 1, step = 0.01),
                     np.arange(start = set_X[:, 1].min() - 1, stop = set_X[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, clsf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.3, cmap = ListedColormap(('blue', 'yellow')))
print ("Accuracy Score is")
print (clsf.score(set_X, set_y))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for k, l in enumerate(np.unique(set_y)):
    plt.scatter(set_X[set_y == l, 0], set_X[set_y == l, 1],
                c = ListedColormap(('blue', 'yellow'))(k), label = l)
plt.title('Testing set')
plt.xlabel('Linear Discriminant 1')
plt.ylabel('Linear Discriminant 2')
#plt.legend()
plt.show()