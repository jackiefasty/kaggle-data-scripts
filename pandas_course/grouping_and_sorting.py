import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Groupwise analysis
reviews.groupby('points').points.count()

# created a group of reviews which allotted the same point 
# values to the given wines. Then, for each of these groups, we grabbed the points() column and counted how many times it appeared.
# Get the cheapest wine in each point value category
reviews.groupby('points').price.min()

# Select the name of the first wine reviewed from each winery in the dataset
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# Get the best wine by country and province
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# Get simple statistical summary of the dataset
reviews.groupby(['country']).price.agg([len, min, max])

# Multi-indexes
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
type(countries_reviewed.index)

# The multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method:
countries_reviewed.reset_index()

# Sorting data
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

countries_reviewed.sort_values(by='len', ascending=False)

countries_reviewed.sort_index()

# Sorting more than one column at a time
countries_reviewed.sort_values(by=['country', 'len'])