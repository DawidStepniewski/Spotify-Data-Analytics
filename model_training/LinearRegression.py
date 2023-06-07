import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error


def linear_regression_model(X_train: pd.DataFrame(), X_test: pd.DataFrame(),
                            y_train: pd.DataFrame(), y_test: pd.DataFrame()) -> (str, float, float):
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    y_pred = lr.predict(X_test)

    mse = mean_squared_error(y_true=y_test, y_pred=y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Root mean squared error of regression model: {np.sqrt(mse)}')
    print(f'Mean absolute error for regression model: {mae}')

    return str(lr), np.sqrt(mse), mae