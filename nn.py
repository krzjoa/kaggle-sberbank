# -*- coidng: utf-8 -*-
from pipeline import TrainPipe, TestPipe
import pandas as pd
from xgboost import XGBRegressor


def get_nn():
    from keras.models import Sequential
    from keras.layers import Dense, InputLayer

    model = Sequential()
    #model.add(InputLayer(290, ))
    model.add(Dense(1000, activation='relu', input_shape=(290,)))
    model.add(Dense(1, activation='relu'))
    model.compile('adam', loss='mse')

    return model

trpipe, tpipe = TrainPipe(), TestPipe()

# Wczytywaie danych
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

# Przetworzenie danych
Xtrain, ytrain = trpipe.transform(train)
Xtest, ids = tpipe.transform(test)

print Xtrain.shape, ytrain.shape


# Train & test

nn = get_nn()

nn.fit(Xtrain, ytrain, verbose=1, epochs=30)

pred = nn.predict(Xtest)

pd.DataFrame.from_dict({"id":ids, 'price_doc':pred.ravel() }).to_csv("results/exp.csv", index=False)




