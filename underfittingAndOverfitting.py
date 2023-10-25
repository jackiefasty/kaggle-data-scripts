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
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))

#function to calculate and get the MAE
def getMae(input_max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=input_max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)

    return(mae) #return the Mean Absolute Value for the given max_leaf_nodes

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

mae_dict = {}
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
for max_leaf_nodes in candidate_max_leaf_nodes:
    mae_dict[max_leaf_nodes] = getMae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(mae_dict[max_leaf_nodes])

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = min(mae_dict, key=mae_dict.get)

# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size,random_state=42)

# fit the final model and uncomment the next two lines
final_model.fit(X, y)