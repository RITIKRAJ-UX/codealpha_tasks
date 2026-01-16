from music21 import stream, note, chord

# Paste generated notes manually OR import from Step-6
generated_notes = [
    'F4', 'G4', 'A4', 'B-4', 'C5', 'B-4', 'A4', 'G4',
    'F4', 'A4', 'C5', 'B-4', 'A4'
]

output_notes = []
offset = 0

for pattern in generated_notes:
    if '.' in pattern:
        notes_in_chord = pattern.split('.')
        chord_notes = []
        for n in notes_in_chord:
            chord_notes.append(note.Note(n))
        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)
    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        output_notes.append(new_note)

    offset += 0.5

midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='generated_music.mid')

print("🎵 MIDI file generated successfully!")
