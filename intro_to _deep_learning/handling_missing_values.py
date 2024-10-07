import pandas as pd
import numpy as np

# Read in all the data
nfl_data = pd.read_csv("../input/nf1playbyplay.csv")

# Set seed for reproducibility
np.random.seed()

# Look at the first five rows of the nf1_data file
# A handful of missing data
nfl_data.head()

# Get number of missing points that we have per column
missing_values_count = nfl_data.isnull().sum()

# Look at the number of missing points in the first ten columns
missing_values_count[0:10]

# How many missing values do we have?
total_cells = np.product(nfl_data.shape)
total_missing = missing_values_count.sum()

# Percent of missing data
percent_missing = (total_missing/total_cells)*100
print(percent_missing)

# Remove all the rows that contain a missing value 
nfl_data.dropna()

# Remove all columns with at least one missing value instead
columns_with_na_dropped = nfl_data.dropna(axis=1)
columns_with_na_dropped.head()

print("Columns in the original dataset: %d \n" % nfl_data.shape[1])
print("Column's with na's dropped: 5d" % columns_with_na_dropped.shape[1])

# Filling in missing values automatically
# Get a small subset of the NFL dataset
subset_nfl_data = nfl_data.loc[:, 'EPA': 'Season'].head()
print(subset_nfl_data)

subset_nfl_data.fillna(method='bfill', axis=0).fillna(0)
