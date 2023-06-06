from music21 import chord, stream, note, midi

def chord_progression_to_midi(chord_progression, filename):
    # Create a music21 stream object to hold the notes and chords
    music_stream = stream.Stream()

    for chords in chord_progression:
        # For each chord in the progression, create a music21 chord object
        c = chord.Chord(chords)
        # Add the chord to the stream
        music_stream.append(c)

    # Once all the chords have been added to the stream, write the stream to a MIDI file
    mf = midi.translate.streamToMidiFile(music_stream)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()

# Test with a simple chord progression
chord_progression = [["C4", "E4", "G4"], ["F4", "A4", "C5"], ["G4", "B4", "D5"], ["C4", "E4", "G4"]]
filename = "chord_progression.mid"
chord_progression_to_midi(chord_progression, filename)
