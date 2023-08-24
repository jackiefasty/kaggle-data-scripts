import pandas as pd

# save the filepath to a var for an easier access
melbourne_filepath = 'datasets/melb_data.csv'

#reaad data and store it into a DataFrame var
mb_df = pd.read_csv(melbourne_filepath)

#print a summary of the data in Melbourne data
print("Info of the dataset: "); mb_summary = mb_df.info()
print("Description of the dataset: "); print(mb_df.describe())

#print the first 8 rows of the dataset in a table, for each column (feature)
print("Dataframe: "); print(mb_df.head(8))