import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn import train_test_split
from sklearn.metrics import mean_absolute_error

#load the data
melbourne_file_path = 'datasets/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

#choose target and features
y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# Separate in train and test datasets
train_X, train_y, val_X, val_y = train_test_split(X, y)

# Define model
forest_model = RandomForestRegressor()

# Fit the model
forest_model.fit(train_X, train_y)

# TRain the model by calculating the predictions
forest_model.predict(val_y)

# Predictions
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))