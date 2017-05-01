import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

from pipeline import common_pipe
from utils import rmsle

# Wyczytywanie danych

train = pd.read_csv("data/train.csv")

train = common_pipe(train)


X = train[['full_sq', 'life_sq', 'floor', 'max_floor', 'year', 'month',
           'build_year', 'num_room']].values
y = train.price_doc.values



# Model
reglin = XGBRegressor()

# Cross-walidacja
kf = KFold(n_splits=5, shuffle=True, random_state=42)

results = []

for tr, ts in kf.split(X):
    Xtrain, ytrain = X[tr], y[tr]
    Xtest, ytest = X[ts], y[ts]

    reglin.fit(Xtrain, ytrain)
    pred = reglin.predict(Xtest)

    mse = rmsle(ytest, pred)
    print mse
    results.append(mse)

print "Mean", np.mean(results)
