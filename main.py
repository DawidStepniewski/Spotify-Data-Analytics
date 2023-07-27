import numpy as np
import spotipy
from sklearn.ensemble import RandomForestRegressor
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import model_training
from model_training import build_model, hyperparameter_tuning, tune_model, evaluate_model, \
    LinearRegression, LassoRegression, RidgeRegression
from acquiring_data import preprocessing_data

if __name__ == "__main__":
    def main():
        X_test = pd.read_pickle('Data/Train Test Data/X_test.pickle')
        X_train = pd.read_pickle('Data/Train Test Data/X_train.pickle')
        y_test = pd.read_pickle('Data/Train Test Data/y_test.pickle')
        y_train = pd.read_pickle('Data/Train Test Data/y_train.pickle')
        model_performance = pd.DataFrame(columns=['Name', 'RMSE', 'MAE'])

        linear_regression = LinearRegression.linear_regression_model(X_train, X_test, y_train, y_test)
        lasso_regression = LassoRegression.lasso_regression_model(X_train, X_test, y_train, y_test)
        ridge_regression = RidgeRegression.ridge_regression_model(X_train, X_test, y_train, y_test)

        model_performance.loc[len(model_performance)] = linear_regression
        model_performance.loc[len(model_performance)] = lasso_regression
        model_performance.loc[len(model_performance)] = ridge_regression
        print(model_performance)

    main()
