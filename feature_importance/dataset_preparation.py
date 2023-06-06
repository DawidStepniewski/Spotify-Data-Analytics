import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def scale_dataframe(dataframe: pd.DataFrame()):
    X = dataframe.drop('y', axis=1)
    y = dataframe['y']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)