import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from model_training import pipeline, hyperparameter_tuning, evaluate_model


def ridge_regression_model(X_train: pd.DataFrame(), X_test: pd.DataFrame(),
                            y_train: pd.DataFrame(), y_test: pd.DataFrame()) -> (str, float, float):

    model = Ridge(random_state=42)
    ridge_pipeline = pipeline.create_pipeline(model=model)
    ridge_param_grid = {
        'model__alpha': np.arange(0.00, 1.0, 0.01)
    }
    lasso_model = hyperparameter_tuning.tune_hyperparameters(pipeline=ridge_pipeline, param_grid=ridge_param_grid,
                                                             X_train=X_train, y_train=y_train)
    rmse, mse = evaluate_model.evaluate_model_performance(lasso_model, X_test, y_test)

    return str(model), rmse, mse
