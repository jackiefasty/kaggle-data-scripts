import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

# Display the full dataframe
reviews

# Takes the elements of the column 'country'
reviews.country

# Takes the elements of the column 'country', same as the previos
reviews['country']

# Takes the elements of the column 'country',
# which the value at index 0 in the country column
reviews['country'][0]

# Takes all the elements from the dataframe, located at 0
reviews.iloc[0]

# Takes all the elements from the dataframe, from column 0
reviews.iloc[:, 0]

# Takes the elements from the beginning to the 3rd
# :3: This selects the rows from index 0 to index 2 (since Python uses zero-based indexing, index 3 is excluded). It selects the first three rows.
# 0: This selects the column at index 0. So, it selects the first column.
reviews.iloc[:3, 0]

# Takes the elements from indexes 1 to 3
reviews.iloc[1:3, 0]

# Takes the elements with indexes 0, 1 and 2
reviews.iloc[[0,1,2], 0]

# .iloc is simpler than loc since ignores the indices of the dataset. 
# Takes the elements from the 5th to the 0 starting from the end of the DataFrame
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

