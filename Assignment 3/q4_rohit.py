# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 16:35:32 2018

@author: rabhishe
"""
#Importing the libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.cross_validation import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import datasets, metrics


#Using Iris dataset
irisdataset=datasets.load_iris()
X_set=irisdataset.data
y_set=irisdataset.target


#K Neighbors without Cross Validation
k_neighbor_range=range(1,151)
score=[]
for K in k_neighbor_range:
    K_model_without_cross_validation=KNeighborsClassifier(n_neighbors=K)
    K_model_without_cross_validation.fit(X_set,y_set)
    print("Accuracy for",K,"=",K_model_without_cross_validation.score(X_set,y_set))
    score.append(K_model_without_cross_validation.score(X_set,y_set))

import matplotlib.pyplot as plt

plt.plot(k_neighbor_range,score)
plt.xlabel("K Value (Without cross Validation)")
plt.ylabel("Accuracy")
plt.show()

#K Neighbors with Cross Validation
X_training,X_testing,y_training,y_testing=train_test_split(X_set,y_set,test_size=0.2)

#testing and training data
model= KNeighborsClassifier(n_neighbors=5)
model.fit(X_training,y_training)

y_pred=model.predict(X_testing)


k_neighbor_range=range(1,121)
score=[]

for K in k_neighbor_range:
    k_nearest_n=KNeighborsClassifier(n_neighbors=K)
    k_nearest_n.fit(X_training,y_training)
    y_prediction=k_nearest_n.predict(X_testing)
    score.append(metrics.accuracy_score(y_testing,y_prediction))

import matplotlib.pyplot as plt

plt.plot(k_neighbor_range,score)
plt.xlabel("K Value (Cross Validation)")
plt.ylabel("Accuracy")
plt.legend ()
plt.show()
