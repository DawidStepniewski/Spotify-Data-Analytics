import numpy as np
from model_training import hyperparameter_tuning
from sklearn.ensemble import RandomForestRegressor

def tune_rf_model(X_train, y_train):
    rf = RandomForestRegressor()
    param_grid = {'n_estimators': [int(x) for x in np.linspace(start=200, stop=2000, num=10)],
               'max_features': ['auto', 'sqrt'],
               'max_depth': [int(x) for x in np.linspace(10, 100, num=10)],
               'min_samples_split': [2, 5, 10],
               'min_samples_leaf': [1, 2, 4],
               'bootstrap': [True, False]}
    best_estimator = hyperparameter_tuning.tune_hyperparameters(rf, param_grid, X_train, y_train)
    print(best_estimator)

