import numpy as np


def rmsle(y_true, y_pred):
    return np.sqrt(((np.log(y_pred + 1) - np.log(y_true+1))**2).mean())