import pandas as pd
from tensorflow import keras
from keras import Sequential, layers

# Adding dropout
keras.Sequential(
    layers.Dropout(rate=0.2),  # Appling 20% dropout to the next layer
    layers.Dense(16)
)

# Adding batch normalization
layers.Dense(16, activation='relu')
layers.BatchNormalization(),
layers.Dense(16),
layers.BatchNormalization(),
layers.Activation('relu')

model = keras.Sequential({
    layers.Dense(1024, activation='relu', input_shape=[11]),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(1024, activation='relu'),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(1024, activation='relu'),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(1),
})

model.compile(
    optimizer='adam',
    loss='mae'
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_valida, y_valid),
    batch_size=256,
    epochs=100,
    verbose=0
)

history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot(); 