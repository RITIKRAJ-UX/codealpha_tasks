import numpy as np
import pickle

# ---------------- LOAD NOTES ----------------
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

print("Total notes loaded:", len(notes))
print("Sample notes:", notes[:20])

# ---------------- PREPARE TRAINING SEQUENCES ----------------
unique_notes = sorted(set(notes))
note_to_int = {note: num for num, note in enumerate(unique_notes)}

sequence_length = 100
X = []
y = []

for i in range(len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length]

    X.append([note_to_int[n] for n in seq_in])
    y.append(note_to_int[seq_out])

X = np.reshape(X, (len(X), sequence_length, 1))
X = X / float(len(unique_notes))

print("Total sequences created:", len(X))
print("Input shape:", X.shape)
print("Sample X[0] (first 10 values):", X[0][:10])
print("Sample y[0]:", y[0])

# ---------------- SAVE FOR NEXT STEP ----------------
pickle.dump(X, open("X.pkl", "wb"))
pickle.dump(y, open("y.pkl", "wb"))
pickle.dump(note_to_int, open("note_to_int.pkl", "wb"))

print("Training data saved: X.pkl, y.pkl, note_to_int.pkl")
