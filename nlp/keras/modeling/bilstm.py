from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional, SpatialDropout1D, Conv1D, Dropout

def build_model(word_index, max_len):

    model = Sequential()
    model.add(Embedding(len(word_index) + 1, 100))
    # model.add(Embedding(len(word_index) + 1,
    #                     100,
    #                     weights=[embedding_matrix],
    #                     input_length=max_len,
    #                     trainable=False))
    model.add(SpatialDropout1D(0.2))
    model.add(Conv1D(64, 5, activation='relu'))
    model.add(Bidirectional(LSTM(100, dropout=0.3, recurrent_dropout=0.3)))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
    model.summary()

    return model
    