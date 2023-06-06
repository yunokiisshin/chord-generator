from music21 import *
from chord_map import *

def chord_progression_to_midi(chord_progression, note_length, filename):
    # Create an empty music21 stream object to hold the notes and chords
    music_stream = stream.Stream()

    for chords in chord_progression:
        # For each chord in the progression, create a music21 chord object
        c = chord.Chord(chords, duration=duration.Duration(note_length))
        # Add the chord to the stream
        music_stream.append(c)

    # Once all the chords have been added to the stream, write the stream to a MIDI file
    mf = midi.translate.streamToMidiFile(music_stream)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()

def main(note_length = 2.0, chord_progression = [["C4", "E4", "G4"], ["F4", "A4", "C5"], ["G4", "B4", "D5"], ["C4", "E4", "G4"]]):
    # Test with a simple chord progression
    filename = "./result/chord_progression.mid"
    chord_progression_to_midi(chord_progression, note_length, filename)
    
if __name__ == "__main__":
    main()