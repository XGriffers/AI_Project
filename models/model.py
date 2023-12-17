# model.py
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split




def prepare_data(x, y):
    x_train, y_train, x_test, y_test = train_test_split(x, y, test_size=0.2)
     # Convert labels to integer encoding
    y_train = np.array(y_train).astype(np.int32)
    y_test = np.array(y_test).astype(np.int32)

    return x_train, y_train, x_test, y_test


def create_model(vocab_size, max_length, embedding_dim=256):

    
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length))
    model.add(LSTM(units=32, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=64))
    model.add(Dense(units=vocab_size, activation='relu'))
    model.compile(optimizer='SGD', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    return model
