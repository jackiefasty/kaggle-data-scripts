# Import packages
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/train.csv'

home_data = pd.read_csv(iowa_file_path)

# Create target object and call it 'y'
y = home_data.SalePrice

# Create X vector
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model 
iowa_model = DecisionTreeRegressor(X, y, random_state=1)

# Fit model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate MAE
val_predictions = iowa_model.predict(val_X) 
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

# Using the best value for finding the maximum number of leafs, max_leaf_nodes
iowa_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
iowa_model.fit(train_X, train_y)
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))

# Exercises: use a Random Forest
from sklearn.ensemble import RandomForestRegressor

# Define the model and set random_state as 1
rf_model = RandomForestRegressor(X, y, random_state=1)

# Fit the model
rf_model.fit(train_X, train_y)

# Calculate the MAE of your RF model on the validation data
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

# Print the validation for the MAE for RF model
print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))



