import numpy as np
import pickle
from tensorflow.keras.models import load_model

print("===== MUSIC GENERATION STARTED =====")

# ---------------- LOAD FILES ----------------
X = pickle.load(open("X.pkl", "rb"))
note_to_int = pickle.load(open("note_to_int.pkl", "rb"))

model = load_model("best_model.h5")

unique_notes = len(note_to_int)

# Reverse dictionary (number → note)
int_to_note = {num: note for note, num in note_to_int.items()}

sequence_length = X.shape[1]

# ---------------- SELECT RANDOM SEED ----------------
start = np.random.randint(0, len(X) - 1)
pattern = X[start]

print("Seed selected. Generating music...")

# ---------------- GENERATE NOTES ----------------
generated_notes = []

for i in range(200):
    prediction = model.predict(
        pattern.reshape(1, sequence_length, 1),
        verbose=0
    )

    index = np.argmax(prediction)
    result = int_to_note[index]
    generated_notes.append(result)

    # Update pattern (sliding window)
    pattern = np.append(
        pattern,
        [[index / float(unique_notes)]],
        axis=0
    )
    pattern = pattern[1:]

print("Music generation completed!")
print("Generated notes:")
print(generated_notes[:30])
