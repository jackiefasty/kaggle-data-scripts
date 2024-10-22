import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import mutual_info_regression
import matplotlib as plt
import seaborn as sns
import numpy as np

X = df.copy()
y = X.pop("price")

# Label encoding for categoricals
for col_name in X.select_dtypes("objects"):
    X[col_name], _ = X[col_name].factorize()

# All discrete features should now have integer dtypes
discrete_features = X.dtypes == int

def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)

    return mi_scores

mi_scores = make_mi_scores(X, y, discrete_features)
mi_scores[::3]

def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")

plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores)

sns.relplot(x="curb_weight", y="price", data=df)

sns.lmplot(x="horsepower", y="price", hue="fuel_type", data=df); 