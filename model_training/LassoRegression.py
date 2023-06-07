import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from model_training import pipeline, hyperparameter_tuning, evaluate_model


def lasso_regression_model(X_train: pd.DataFrame(), X_test: pd.DataFrame(),
                            y_train: pd.DataFrame(), y_test: pd.DataFrame()) -> (str, float, float):

    model = Lasso(random_state=42)
    lasso_pipeline = pipeline.create_pipeline(model=model)
    lasso_param_grid = {
        'model__alpha': np.arange(0.00, 1.0, 0.01)
    }
    lasso_model = hyperparameter_tuning.tune_hyperparameters(pipeline=lasso_pipeline, param_grid=lasso_param_grid,
                                                             X_train=X_train, y_train=y_train)
    rmse, mse = evaluate_model.evaluate_model_performance(lasso_model, X_test, y_test)

    return str(model), rmse, mse
