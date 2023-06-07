from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline


def create_pipeline(model):
    one_hot_encoder = ColumnTransformer(
        transformers=[('one hot encode', OneHotEncoder(handle_unknown='ignore'), ['key'])], remainder='passthrough')
    pipeline = Pipeline(steps=[('one hot encode', one_hot_encoder),
                               ('scaler', StandardScaler()),
                               ('model', model)])

    return pipeline
