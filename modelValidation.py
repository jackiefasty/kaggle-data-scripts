import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

#-------Build the model-------
#load the data
# save the filepath to a var for an easier access
melbourne_file_path = 'datasets/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

#filter rows with missing price values, dropna drops the missing values, axis=0 means rows
filtered_melbourne_data = melbourne_data.dropna(axis=0)

#choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

melbourne_model = DecisionTreeRegressor(random_state=1)

#melbourne_model.fit(X, y)

#calculate prediction error
#predicted_home_prices = melbourne_model.predict(X)

#calculate mean absolute percentage error
#mean_absolute_error(y,predicted_home_prices)

#-------Split the data into training and validation data-------

#split the data into training and validation data, for both features and target
#The split is randomized . If we give a numeric value to the random_state argument
#we get the same split every time we run the script
train_X, validate_X, train_y, validate_y = train_test_split(X, y, random_state=0)

#define the model
melbourne_model = DecisionTreeRegressor()

#fit the model
melbourne_model.fit(train_X, train_y)

#get predicted prices on validation set
val_predict = melbourne_model.predict(validate_X)
print("The mean absolute error is: "); print(mean_absolute_error(validate_y, val_predict))

#--------CODE PART--------
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

#define the model
melbourne_model = DecisionTreeRegressor()

#fit the model
melbourne_model.fit(train_X, train_y)

#get the predicticted prices
valuesOfThePredictions = melbourne_model.predict(val_X)
print(mean_absolute_error((val_y, valuesOfThePredictions)))

