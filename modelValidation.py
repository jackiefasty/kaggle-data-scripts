import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error

# save the filepath to a var for an easier access
melbourne_filepath = 'datasets/melb_data.csv'

melbourne_model = DecisionTreeRegressor(random_state=1)

#calculate prediction error
predicted_home_prices = melbourne_model.predict(X)

#calculate mean absolute percentage error
mean_absolute_error(y,predicted_home_prices)