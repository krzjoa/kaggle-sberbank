# -*- coidng: utf-8 -*-
from pipeline import TrainPipe, TestPipe
import pandas as pd
from xgboost import XGBRegressor


trpipe, tpipe = TrainPipe(), TestPipe()

# Wczytywaie danych
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

# Przetworzenie danych
Xtrain, ytrain = trpipe.transform(train)
Xtest, ids = tpipe.transform(test)

print Xtrain.shape, ytrain.shape


# Train & test
xgb_reg = XGBRegressor()

xgb_reg.fit(Xtrain, ytrain)

pred = xgb_reg.predict(Xtest)

pd.DataFrame.from_dict({"id":ids, 'price_doc':pred }).to_csv("results/exp.csv", index=False)


