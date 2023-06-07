import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error


def evaluate_model_performance(model, X_test, y_test):
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_true=y_test, y_pred=y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true=y_test, y_pred=y_pred)

    print(f'{str(model)}:')
    print(f'Root mean squared error: {rmse}')
    print(f'Mean absolute error: {mae}')

    return rmse, mae
