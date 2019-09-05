import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, LSTM, Dense


def vanilaLSTM(input_shape, output_shape):
    model = Sequential()
    model.add(LSTM(300, input_shape=(input_shape)))
    model.add(Dropout(rate=0.2))
    model.add(Dense(output_shape, activation='softmax'))
    optimizer = keras.optimizers.Adam(lr=0.001, decay=1e-6)
    model.compile(optimizer, loss="categorical_crossentropy",metrics=['accuracy'])

    return model


def LSTMv1(input_shape, output_shape):
    model = Sequential()
    model.add(LSTM(300, input_shape=(input_shape)))
    model.add(Dropout(rate=0.2))
    model.add(Dense(300, activation='relu'))
    model.add(Dropout(rate=0.2))
    model.add(Dense(output_shape, activation='softmax'))
    optimizer = keras.optimizers.Adam(lr=0.001, decay=1e-6)
    model.compile(optimizer, loss="categorical_crossentropy",metrics=['accuracy'])

    return model
