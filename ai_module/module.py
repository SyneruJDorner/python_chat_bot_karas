import sys, os
file_path = os.path.dirname(os.path.abspath(__file__))

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

def brain(settings, train_x, train_y):
    model = Sequential()
    model.add(Dense(settings['node_density_1'], input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(settings['dropout_rate_1']))
    model.add(Dense(settings['node_density_2'], activation='relu'))
    model.add(Dropout(settings['dropout_rate_2']))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    # Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
    sgd = SGD(lr=settings['lr'], decay=settings['decay'], momentum=settings['momentum'], nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    return model

def save_brain(settings, model, train_x, train_y):
    hist = model.fit(np.array(train_x), np.array(train_y), epochs=settings['epochs'], batch_size=settings['batch_size'], verbose=settings['verbose'])
    model.save(os.path.join(os.path.dirname(file_path), "trained_data\\chatbot_model.h5"), hist)