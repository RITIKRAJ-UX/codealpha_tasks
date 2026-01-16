from music21 import converter, instrument, note, chord
import glob

notes = []

# Correct path to your MIDI files
midi_files = glob.glob(
    r"C:\Users\rs182\OneDrive\Desktop\AI_Music_Project\music_dataset\*.mid"
)

for file in midi_files:
    print("Processing:", file)
    midi = converter.parse(file)
    parts = instrument.partitionByInstrument(midi)

    if parts:
        elements = parts.parts[0].recurse()
    else:
        elements = midi.flat.notes

    for element in elements:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

print("\nTotal Notes Extracted:", len(notes))
print("Sample Notes:", notes[:20])


import pickle

# Save extracted notes to file
with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("Notes saved successfully as notes.pkl")

