from __future__ import division, print_function, absolute_import
import tflearn
import tflearn.datasets.mnist as mnist
import cv2
import numpy as np


def buildModel():
    # Building deep neural network
    input_layer = tflearn.input_data(shape=[None, 784])
    dense1 = tflearn.fully_connected(input_layer, 64, activation='tanh',
                                     regularizer='L2', weight_decay=0.001)
    dropout1 = tflearn.dropout(dense1, 0.8)
    dense2 = tflearn.fully_connected(dropout1, 64, activation='tanh',
                                     regularizer='L2', weight_decay=0.001)
    dropout2 = tflearn.dropout(dense2, 0.8)
    softmax = tflearn.fully_connected(dropout2, 10, activation='softmax')
    # Regression using SGD with learning rate decay and Top-3 accuracy
    sgd = tflearn.SGD(learning_rate=0.1, lr_decay=0.96, decay_step=1000)
    top_k = tflearn.metrics.Top_k(3)
    net = tflearn.regression(softmax, optimizer=sgd, metric=top_k,
                             loss='categorical_crossentropy')
    # Training
    model = tflearn.DNN(net, tensorboard_verbose=0)
    return model


def train(model, X, Y, testX, testY):
    model.fit(X, Y, n_epoch=15, validation_set=(testX, testY),
              show_metric=True, run_id="dense_model")


def save(model, filename):
    model.save(filename)


def load(model, filename):
    model.load(filename)


def predict(model, imageVec):
    return np.argmax(model.predict(imageVec))

def showImage(image):
    cv2.imshow('image', image.reshape(28,28))
    cv2.waitKey(0)

model = buildModel()
X, Y, testX, testY = mnist.load_data(one_hot=True)

#train(model,X,Y,testX,testY)
#save(model, 'mnist.model')
load(model,'mnist.model')

for i in range(0,10):
    showImage(testX[i])
    print (predict(model, [testX[i]]))