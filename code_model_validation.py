import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

#load the data
melbourne_file_path = 'datasets/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

#filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)

#choose target and features
y = filtered_melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

#split the data into training and validation data, both for features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we

#define the model
melbourne_model = DecisionTreeRegressor()

#fit model
melbourne_model.fit(X,y)

#calculate now the MAE
predicted_home_prices = melbourne_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))