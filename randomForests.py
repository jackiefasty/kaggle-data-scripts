from sklearn.ensamble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Define model
forest_model = RandomForestRegressor()
forest_model.fit(train_X, train_y)

# Predictions
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))