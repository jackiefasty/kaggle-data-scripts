import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Display dataframe
reviews

# Summary functions
reviews.points.describe()

# Summary functions and describe "taster_name"
reviews.taster_name.describe()

# See mean value of values in column "points"
reviews.points.mean()

# See unique values on column "taster_name"
reviews.taster_name.unique()

# See list of unique values and how often they occur in a dataset
reviews.taster_name.value_counts()

# Display maps
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

reviews.head(1)

# Common mapping operation
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

# Easier like this
reviews.country + " - " + reviews.region_1



