# Set up code checking
from learntools.core import binder
import os
binder.bind(globals())
from learntools.machine_learning.ex7 import *

# Set up filepaths
import os
if not os.path.exists("../datasets/train.csv"):
    os.symlink("../input/home-data-for-ml-course/train.csv", "../input/train.csv")  
    os.symlink("../input/home-data-for-ml-course/test.csv", "../input/test.csv")

# Import helpful libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the data, and separate the target
iowa_file_path = '../input/train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice

# Creta X (After completing the excercise, return to modify this line)
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Select the columns corresponding to features, and preview the data
X = home_data[features]
X.head()

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X,y, random_state=1)

# Define a random forest model
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))

# Train a model for the competition

# To improve accuracy, create a new RandomForest model which you will train
# on all training data
rf_model_on_all_data = RandomForestRegressor()

# Fit the rf_model_on_full_data on all data from the training data
rf_model_on_all_data.fit(train_X, train_y)

# Set the path to the file to be used for predictions
test_data_path = '../datasets/test.csv'

# Read test data file using pandas
test_data = pd.read_csv(test_data_path)

# Create test_X which comes from test_data but includes only
# columns to be used by the list of columns stored in 'features'
text_X = test_data[features]

# Make predictions to be submitted
test_preds = rf_model_on_all_data.predict(val_X)

# Run the code to save predictions in the format used for competition scoring
output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)