import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

reviews

reviews.country

reviews['country']

reviews['country'][0]

reviews.iloc[0]

reviews.iloc[:, 0]

reviews.iloc[:3, 0]

reviews.iloc[1:3, 0]

reviews.iloc[[0,1,2], 0]

reviews.iloc[-5:0]

# .loc uses the information in the indexes to do its job
reviews.loc[0, 'country']

# .loc uses the information in the indexes to do its job
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

# Manipulating the index
reviews.set_index("title")

# Select those reviews whose country is Italy
reviews.country == 'Italy'

# Take the reviews 
reviews.loc[reviews.country == 'Italy']

# Buy wine made in Italy and that has a puntuation of more than 90
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

# Buy wine made in Italy or that has a puntuation of more than 90
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

