# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:33:28 2018

@author: rabhishe
"""

#!/usr/bin/env python

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data


#Extracting and loading the dataset to folder data. One hot vector is being used for each label here.
dataset_mnist = input_data.read_data_sets('data/', one_hot=True)


#Defining the parameters for logistic regression
learning_rate = 0.001
training_epochs = 50
batch_size = 500

#create the placeholders for features and labels
x_placeholder = tf.placeholder("float", [None, 784])
y_placeholder = tf.placeholder("float", [None, 10])

#Defining the weights and the bias
weight_W = tf.Variable(tf.ones([784,10]))
bias_b = tf.Variable(tf.zeros([10]))

#6.	Constructing the model by Activation, Cost,Optimizing functions
##Softmax regression/Multinomial logistics regression 
prediction = tf.nn.softmax(tf.matmul(x_placeholder,weight_W) + bias_b) 
#c_function indicates the cross-entropy function. 
c_function = tf.reduce_mean(-tf.reduce_sum(y_placeholder*tf.log(prediction), reduction_indices=1))
#optimizer function is used for initialization of the Optimizer
optimizer_function = tf.train.GradientDescentOptimizer(learning_rate).minimize(c_function)

#Gradient Descent
p = tf.equal(tf.argmax(prediction, 1), tf.argmax(y_placeholder,1))
accuracy = tf.reduce_mean(tf.cast(p, "float"))


with tf.Session() as session:
    session.run(tf.initialize_all_variables()) #Initialize the variables
    writer = tf.summary.FileWriter('./graphs/logistic_reg', session.graph)
	
    #Training the model
    for epoch in range(training_epochs):
        loss = 0
        batch = int(dataset_mnist.train.num_examples/batch_size)
		
        #Looping over all batches
        for i in range(batch):
         x1, y1= dataset_mnist.train.next_batch(batch_size)
            #Runing the optimization and calculating the loss for each batch size
        _, cst = session.run([optimizer_function, c_function], feed_dict={x_placeholder: x1,
                                                          y_placeholder: y1})
            #average loss
        loss += cst / batch
        # Displaying the  logs per epoch step 
        print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(loss))
    writer.close()
    weight_W, bias_b = session.run([weight_W, bias_b])
    
    #testing the model and calculating the accuracy of the model and printing the accuracy.   
    correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y_placeholder, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy :", accuracy.eval({x_placeholder: dataset_mnist.test.images, y_placeholder: dataset_mnist.test.labels}))
  
