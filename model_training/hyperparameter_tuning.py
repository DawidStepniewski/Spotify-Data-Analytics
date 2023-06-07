from sklearn.model_selection import RandomizedSearchCV


def tune_hyperparameters(pipeline, param_grid, X_train, y_train):
    gs = RandomizedSearchCV(estimator=pipeline,
                            param_distributions=param_grid,
                            verbose=3,
                            cv=3,
                            n_jobs=-1,
                            scoring='neg_mean_squared_error',
                            random_state=42,
                            n_iter=50)
    gs.fit(X_train, y_train.values.ravel())
    return gs.best_estimator_
