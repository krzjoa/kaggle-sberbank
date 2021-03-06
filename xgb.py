import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

from pipeline import common_pipe
from utils import rmsle, non_negative

from sklearn.preprocessing import StandardScaler
from ensemble import EnsembleRegressor

# Wyczytywanie danych

train = pd.read_csv("data/train.csv")

train = common_pipe(train)


X = train.values
y = train.price_doc.values

scaler = StandardScaler()

# Model
xgb = XGBRegressor(n_estimators=200, learning_rate=0.2, max_depth=3)
reglin = EnsembleRegressor(main_estimator=xgb)


# Cross-walidacja
kf = KFold(n_splits=5, shuffle=True, random_state=42)

results = []

for tr, ts in kf.split(X):
    Xtrain, ytrain = X[tr], y[tr]
    Xtest, ytest = X[ts], y[ts]

    Xtrain = scaler.fit_transform(Xtrain)
    Xtest = scaler.transform(Xtest)

    reglin.fit(Xtrain, ytrain)
    pred = reglin.predict(Xtest)

    #print pred.sum()

    mse = rmsle(ytest, non_negative(pred))
    print mse
    results.append(mse)

print "Mean", np.mean(results)
