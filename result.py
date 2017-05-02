# -*- coidng: utf-8 -*-
from pipeline import TrainPipe, TestPipe
import pandas as pd
from xgboost import XGBRegressor
from ensemble import EnsembleRegressor

trpipe, tpipe = TrainPipe(), TestPipe()

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LinearRegression

scaler = StandardScaler()

# Wczytywaie danych
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

# Przetworzenie danych
Xtrain, ytrain = trpipe.transform(train)
Xtest, ids = tpipe.transform(test)

Xtrain = scaler.fit_transform(Xtrain)
Xtest = scaler.transform(Xtest)

#print Xtrain.shape, ytrain.shape


xgb = XGBRegressor(n_estimators=200, learning_rate=0.2, max_depth=3)
reg = EnsembleRegressor(xgb)


# Train & test


reg.fit(Xtrain, ytrain)

pred = reg.predict(Xtest)

print "Negative", (pred < 0).sum()

pd.DataFrame.from_dict({"id":ids, 'price_doc':pred }).to_csv("results/exp2.csv", index=False)


