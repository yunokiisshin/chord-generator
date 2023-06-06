# basic_bc.py

from music21 import chord, stream, note, midi, duration
from chord_map import major_triad, minor_triad, major_seventh, minor_seventh, dominant_seventh

def chord_progression_to_midi(chord_symbols, note_length, filename):
    # Create a music21 stream object to hold the notes and chords
    music_stream = stream.Stream()

    for symbol in chord_symbols:
        # Determine the root note and the type of chord
        root_note = symbol[0]
        if symbol[1] in ["#", "b"]:
            root_note += symbol[1]
            chord_type = symbol[2:]
        else:
            chord_type = symbol[1:]

        
        
        # Generate the notes for the chord
        if chord_type == 'M':
            notes = major_triad(root_note)
        elif chord_type == 'm':
            notes = minor_triad(root_note)
        elif chord_type == 'M7':
            notes = major_seventh(root_note)
        elif chord_type == 'm7':
            notes = minor_seventh(root_note)
        elif chord_type == '7':
            notes = dominant_seventh(root_note)
        else:
            raise ValueError(f"Unknown chord type: {chord_type}")

        # Create a music21 chord object with these notes
        c = chord.Chord(notes, duration=duration.Duration(note_length))
        # Add the chord to the stream
        music_stream.append(c)

    # Once all the chords have been added to the stream, write the stream to a MIDI file
    mf = midi.translate.streamToMidiFile(music_stream)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()


def main():
    # Test with a simple chord progression
    chord_symbols = input("list chord progression: ").split()
    print(chord_symbols)
    note_length = 2.0  # Half notes
    filename = "./result/chord_progression.mid"
    chord_progression_to_midi(chord_symbols, note_length, filename)

if __name__ == "__main__":
    main()