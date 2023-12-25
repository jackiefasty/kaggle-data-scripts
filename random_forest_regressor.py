import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'datasets/train.csv'

home_data = pd.read_csv(iowa_file_path)

#create target object and call it y
y = home_data.SalePrice

# Create X, which is an array of the features used for the prediction
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr',
            'TotRmsAbvGrd']

X = home_data[features]

# split data into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

#specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

#fit model
iowa_model.fit(train_X, train_y)

#predict with all validation observations
val_predictions = iowa_model.predict(val_X)

print(val_predictions)

#calculate the MAE, Mean Absolute Error
mae_val = mean_absolute_error(val_predictions, val_y) #column x column

print("Validation MAE when not specifying the maximum number of leaf nodes: {:, .0f}", format(mae_val))

#using the best value for the maximum number of leaf nodes
iowa_model = DecisionTreeRegressor(max_leaf_nodes = 100, random_state=1)
iowa_model.fit(train_X, train_y)
print("val_X: ", val_X); print(np.size())
val_preds = iowa_model.predict(val_X)
max_mae_val = mean_absolute_error(val_preds, val_y)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(max_mae_val))

#Now, use a RF Random Forest
#RF model validation
from sklearn.metrics import RandomForestRegressor

#define the model by setting the random_state at 1
rf_model = RandomForestRegressor(random_state=1)

#fit the model
rf_model.fit(train_X, train_y)

#calculate the MAE of the RF model on the validation data
rf_val_preds = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_preds, val_y)

print("Validation MAE for RF model: {:,.0f}".format(rf_val_mae))


