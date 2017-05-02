import numpy as np


def non_negative(inp):
    inp[inp < 0] = 0
    return inp

def rmsle(y_true, y_pred):
    return np.sqrt(((np.log(y_pred + 1) - np.log(y_true+1))**2).mean())


# def debug_rmsle(y_true, y_pred):
#     logpred = np.log(y_pred+1)
#     logtrue = np.log(y_true+1)
#     logsquare = (logpred - logtrue)**2
#     mean = logsquare.mean()
#     sqr = np.sqrt(mean)
#     print "Negative", (y_pred < 0).sum()
#     print "debug", y_pred.sum(), np.isnan(logpred).sum(), logtrue.sum(), mean, sqr
#     return sqr