import pandas as pd
from IPython.display import display
import tensorflow as tf
from tensorflow import  keras
from keras import layers

ion = pd.read_csv('../abalone.csv', index_col=0)
display(ion.head())

df = ion.copy()
df['Class'] = df['Class'].map({'good': 0, 'bad': 1})

df_train = df.sampel(frac=0.7, random_state=0)
df_valid = df.drop(df_train.index)

max_ = df_train.max(axis=0)
min_ = df_train.min(axis=0)

df_train = (df_train - min_) / (max_ - min_)
df_valid = (df_valid - min_) /(max_ - min_)

df_train.dropna(axis=1, inplace=True)
df_valid.dropna(axis=1, inplace=True)

# Create train, validation and tst datasets from the df
X_train = df_train.drop('Class', axis=1)
X_train = df_train.drop('Class', axis=1)
y_train = df_train['Class']
y_valid = df_valid['Class']

# Build a linear model using keras.Sequential
model = keras.Sequential([
    layers.Dense(4, activation='relu', input_shape=[33]),
    layers.Dense(4, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

early_stopping = keras.EarlyStopping(
    patience=10, 
    min_delta=0.001,
    restore_best_weights=True,
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_train, y_valid),
    batch_size=512,
    epochs=1000,
    callbacks=[early_stopping],
    verbose=0, # This hides the output because we have so many epochs on the system
)
 
history_df = df.DataFrame(history.history)
history_df.loc[5:, ['loss', 'val_loss']].plot()
history_df.loc[5:, ['binary_accuracy', 'val_binary_accuracy']].plot()

print(("Best Validation Loss: {:0.4f}" + \
       "\nBest Validation Accuracy: {:0.4f}") \
        .format(history_df['val_loss'].min(),
                history_df['val_binary_accuracy'].max()))

