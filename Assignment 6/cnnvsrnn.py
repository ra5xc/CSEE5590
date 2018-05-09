import tensorflow as tf
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_1d, global_max_pool
from tflearn.layers.merge_ops import merge
from tflearn.layers.estimator import regression
from tflearn.layers.recurrent import bidirectional_rnn, BasicLSTMCell

# networks
'''
Got them all from https://github.com/tflearn/tflearn/tree/master/examples
just edited and modified a few things according to project needs
'''

def build_conv(max_len, lr=0.001, d_out=0.8):
    '''
    Simple Convolutional network
    '''
    tf.reset_default_graph()
    network = input_data(shape=[None, max_len], name='input')
    network = tflearn.embedding(network, input_dim=10000, output_dim=128)
    branch1 = conv_1d(network, 128, 3, padding='valid', activation='relu', regularizer="L2")
    branch2 = conv_1d(network, 128, 4, padding='valid', activation='relu', regularizer="L2")
    branch3 = conv_1d(network, 128, 5, padding='valid', activation='relu', regularizer="L2")
    network = merge([branch1, branch2, branch3], mode='concat', axis=1)
    network = tf.expand_dims(network, 2)
    network = global_max_pool(network)
    if d_out: network = dropout(network, d_out)
    network = fully_connected(network, 2, activation='softmax')
    network = regression(network, optimizer='adam', learning_rate=lr,
                         loss='categorical_crossentropy', name='target')
    model = tflearn.DNN(network, tensorboard_verbose=0)
    return model

def build_lstm(max_len, lr=0.001, d_out=0.8):
    '''
    Simple Recurrent network
    '''
    tf.reset_default_graph()
    net = input_data([None, max_len])
    net = tflearn.embedding(net, input_dim=10000, output_dim=128)
    net = tflearn.lstm(net, 128, dropout=d_out)
    net = fully_connected(net, 2, activation='softmax')
    net = regression(net, optimizer='adam', learning_rate=lr,
                         loss='categorical_crossentropy')
    model = tflearn.DNN(net, tensorboard_verbose=0)
    return model
    
class CallbackToGetValAcc(tflearn.callbacks.Callback):  
    '''
    Normally, tflearn is a high level library and handles a lot 
    of things for you, the bad thing is you don't have the freedom 
    like TensorFlow. I need to store validation accuracies after 
    each training so I implemented this sub class by inheriting
    tflearn Callback class, it's pretty straightforward, enjoy!
    '''
    def on_train_end(self, training_state):
        final_acc = training_state.val_acc   
        print("Final model accuracy:", final_acc)
        self.val = final_acc
 