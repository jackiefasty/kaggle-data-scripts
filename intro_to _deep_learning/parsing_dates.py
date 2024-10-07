import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# Read in the data from the dataset
landslides = pd.read_csv("../input/landslide-events/catalog.csv")

# Set seed for reproducibility
np.random.seed(0)

landslides.head()

print(landslides['date'].head())
landslides['date'].dtype

# Create a new column, date parsed with the parsed dates
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")

# Print the first few rows
landslides['date_parsed'].head()

# Get the day of the month from the date_parsed column
day_of_month_landslides = landslides['date_parsed'].dt.day
day_of_month_landslides.head()

# Remove the NaN values
day_of_month_landslides = day_of_month_landslides.dropna()

# Plot the day of the month
sns.displot(day_of_month_landslides, kde=False, bins=31)
