from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import AdaBoostRegressor



class EnsembleRegressor(object):

    def __init__(self, main_estimator=None):
        self.main_estimator = main_estimator
        self.aux_regressor = AdaBoostRegressor(base_estimator=LinearRegression(), n_estimators=100)
        #self.lasso = Lasso()


    def fit(self, X, y):
        self.main_estimator.fit(X, y)
        self.aux_regressor.fit(X, y)
        #self.lasso.fit(X, y)
        return self


    def predict(self, X):
        main_pred = self.main_estimator.predict(X)
        aux_pred = self.aux_regressor.predict(X)
        #lasso_pred = self.lasso.predict(X)

        # Korygowanie wynikow
        main_pred[main_pred <=0] = aux_pred[main_pred <=0]
        #main_pred[main_pred <=0] = lasso_pred[main_pred <=0]


        print "Negative", (main_pred <0).sum()

        return main_pred





