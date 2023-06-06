import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def calculate_corr(tracks_data: pd.DataFrame()):
    sns.heatmap(tracks_data.corr(), annot=True, vmin=-1, vmax=1)
    plt.title('Correlation Coefficient of Predictors')
    plt.show()
