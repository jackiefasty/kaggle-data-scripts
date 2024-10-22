from tensorflow import keras
from keras import layers, callbacks
from callbacks import EarlyStopping
import pandas as pd
## Capacity

model = keras.Sequential([
    layers.Dense(16, activation='relu'),
    layers.Dense(1),
])

wider = keras.Sequential([
    layers.Dense(32, activation='relu'),
    layers.Dense(1),
])

deeper = keras.Sequential([
    layers.Dense(16, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(1),
])

# Apply early stopping
early_stopping = callbacks.EarlyStopping(
    min_delta = 0.001, # This is the minimum amout of chnage to count it as an improvement
    patience = 20,
    restore_best_weights = True,
)

model = keras.Sequential(
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1)
)

model.compile(
    optimizer='adam',
    loss='mae',
)

# Now we fit the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    bath_size=256,
    epochs=500,
    callbacks=[early_stopping],
    verbose=0,
)

history_df = pd.DataFrame(history.history); 
history_df.loc[:, ['loss', 'val_loss']].plot(); 
print("Minimum validation loss: {}".format(history_df['val_loss'].min()))