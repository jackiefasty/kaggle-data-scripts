import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

#load the data, path to file
iowa_file_path = '/datasets/train.csv'

home_data = pd.read_csv(iowa_file_path)

#create target object and call it y
y = home_data.SalePrice

#create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath',]
X = home_data[features]

#split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

#specify the model to be trained
iowa_model = DecisionTreeRegressor(random_state=1)

#fit the model
iowa_model.fit(train_X, train_y)

#make validation for the predictions and calculate the MAE
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_y, val_predictions)