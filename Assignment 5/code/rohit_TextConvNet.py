import tensorflow

class TextCNN(object):
    def __init__(
      self, lenght_of_sentense, number_of_class, size_of_the_vocublary,size_of_the_embedding, size_of_the_file, number_of_the_file, l2_reg_lambda=0.0): #sentence lenght,classes lenght,ambedding,vocab

        # Placeholders
        self.input__x_ = tensorflow.placeholder(tensorflow.int32, [None, lenght_of_sentense], name="input_x")
        self.input__y_ = tensorflow.placeholder(tensorflow.float32, [None, number_of_class], name="input_y")
        self.keep__droop = tensorflow.placeholder(tensorflow.float32, name="drop_keep")
        l2_loss = tensorflow.constant(0.0)

        #Embedding layer
        # Embeddings using cpu
        with tensorflow.device('/cpu:0'), tensorflow.name_scope("embedding"):
            # Matrix Embedding
            self.W = tensorflow.Variable(tensorflow.random_uniform([size_of_the_vocublary, size_of_the_embedding], -1.0, 1.0),name="W")
            self.emb_ch = tensorflow.nn.embedding_lookup(self.W, self.input__x_)
            self.emb_ch_exp = tensorflow.expand_dims(self.emb_ch, -1)

        #convolution layer build, shapes,feature vector
        outs = []
        for i, filter_size in enumerate(size_of_the_file):
            with tensorflow.name_scope("conv-maxpool-%s" % filter_size):
                # Convolution layer
                shape_fil = [filter_size, size_of_the_embedding, 1, number_of_the_file]
                Wegt = tensorflow.Variable(tensorflow.truncated_normal(shape_fil, stddev=0.1), name="W")
                b = tensorflow.Variable(tensorflow.constant(0.1, shape=[number_of_the_file]), name="b")
                convolution = tensorflow.nn.conv2d(self.emb_ch_exp,Wegt,strides=[1, 1, 1, 1],padding="VALID",
                                            name="conv")
                h = tensorflow.nn.relu(tensorflow.nn.bias_add(convolution, b), name="relu")
                # Output pooling
                pd = tensorflow.nn.max_pool(h,ksize=[1, lenght_of_sentense - filter_size + 1, 1, 1],strides=[1, 1, 1, 1],
                                                padding='VALID',name="pool")
                outs.append(pd)

        #feature vector
        num_filters_total = number_of_the_file * len(size_of_the_file)
        self.h_pool = tensorflow.concat(outs, 3)
        self.h_pool_flat = tensorflow.reshape(self.h_pool, [-1, num_filters_total])
        #layer of dropout
        with tensorflow.name_scope("dropout"):
            self.h_drop = tensorflow.nn.dropout(self.h_pool_flat, self.keep__droop)

        with tensorflow.name_scope("output"):
            W = tensorflow.get_variable("W",shape=[num_filters_total, number_of_class],
                                        initializer=tensorflow.contrib.layers.xavier_initializer())
            bax = tensorflow.Variable(tensorflow.constant(0.1, shape=[number_of_class]), name="b")
            l2_loss += tensorflow.nn.l2_loss(W)
            l2_loss += tensorflow.nn.l2_loss(bax)
            self.scores = tensorflow.nn.xw_plus_b(self.h_drop, W, b, name="scores")
            self.predictions = tensorflow.argmax(self.scores, 1, name="predictions")

        #loss calculation
        with tensorflow.name_scope("loss"):
            losses__findings= tensorflow.nn.softmax_cross_entropy_with_logits_v2(logits=self.scores, labels=self.input__y_)
            self.loss = tensorflow.reduce_mean(losses__findings) + l2_reg_lambda * l2_loss

        # Accuracy calculation
        with tensorflow.name_scope("accuracy"):
            predicting_correct_prediction = tensorflow.equal(self.predictions, tensorflow.argmax(self.input__y_, 1))
            self.accuracy = tensorflow.reduce_mean(tensorflow.cast(predicting_correct_prediction, "float"), name="accuracy")
