import pandas as pd
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

print(val_X)
