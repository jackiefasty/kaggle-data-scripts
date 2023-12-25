import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Read the data
melbourne_file_path = 'datasets/melb_data.csv'

#read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

#display the column names of the DataFrame
melbourne_data.columns

#dropna drops the missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

#select the prediction target
y = melbourne_data.Price

#choosing features
melbourne_features = ['Rooms', 'Lattitude', 'Longtitude', 'Bathroom', 'Landsize']

#we call the data X
X = melbourne_data[melbourne_features]

#preview the data description 
X.describe()

#get first 5 rows of the data
X.head()

#build the ML model

#define the model and specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

#fit the model
melbourne_model.fit(X, y)

#make predictions for the first few rows of the training data
print("Make predictions for the following 5 houses of the dataset: ")
print(X.head())
print("The predictions are: ")
print(melbourne_model.predict(X.head()))

#calculate the mean absolute error
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

#define the model. Specify a number for random_state to ensure same results each run
rf_model = RandomForestRegressor(random_state=1)

#define the model
#rf_model.fit(train_X, train_y)

