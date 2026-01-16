import pickle
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint

print("===== SCRIPT STARTED =====")

# ---------------- LOAD DATA ----------------
X = pickle.load(open("X.pkl", "rb"))
y = pickle.load(open("y.pkl", "rb"))
note_to_int = pickle.load(open("note_to_int.pkl", "rb"))

unique_notes = len(note_to_int)

print("X shape:", X.shape)
print("y length:", len(y))
print("Unique notes:", unique_notes)

# ---------------- BUILD MODEL ----------------
model = Sequential()

model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(256))
model.add(Dense(256))
model.add(Dense(unique_notes, activation='softmax'))

# ---------------- COMPILE MODEL ----------------
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam'
)

model.summary()

# ---------------- TRAIN MODEL ----------------
epochs = 30
batch_size = 64

checkpoint = ModelCheckpoint(
    "best_model.h5",
    monitor="loss",
    save_best_only=True,
    mode="min"
)

print("===== TRAINING START =====")

model.fit(
    X,
    np.array(y),
    epochs=epochs,
    batch_size=batch_size,
    callbacks=[checkpoint]
)

print("===== TRAINING END =====")
