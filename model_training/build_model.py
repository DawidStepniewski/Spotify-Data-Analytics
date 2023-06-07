import pandas as pd
import pickle
from sklearn.model_selection import train_test_split


def build_model(data: pd.DataFrame()):
    predictors = ['danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                  'liveness', 'valance', 'tempo', 'duration_s', 'key']
    target = ['popularity']

    X = data[predictors]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

    with open('X_train.pickle', 'wb') as files:
        pickle.dump(X_train, files)

    with open('X_test.pickle', 'wb') as files:
        pickle.dump(X_test, files)

    with open('y_train.pickle', 'wb') as files:
        pickle.dump(y_train, files)

    with open('y_test.pickle', 'wb') as files:
        pickle.dump(y_test, files)

