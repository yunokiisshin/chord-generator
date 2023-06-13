#chord_to_midi.py: １小節１コード、リズムなしのシンプルなMIDI書き出し担当

# maybe think about post-generation? Like adding a filter that shifts chords around
# when the chord voicing is too high up, by calculating the sum of note values?

from music21 import *
from modules.chord_map_custom import *

def block_chords_to_midi(chord_symbols, note_length, epoch, mode):
    # Create a music21 stream object to hold the notes and chords
    music_stream = stream.Stream()
    for i in range(4):
        chord_name = ""
        for symbol in chord_symbols:
            chord_name = chord_name + symbol + "_"
            # Determine the root note and the type of chord
            root_note = symbol[0]
            if symbol[1] in ["#", "b"]:
                root_note += symbol[1]
                chord_type = symbol[2:]
            else:
                chord_type = symbol[1:]
            
            # Generate the notes for the chord
            
            #balancing the sound range of chords
            root_note += "4"
            
            if chord_type == 'M':
                notes = major_triad(root_note,mode) 
            elif chord_type == 'm':
                notes = minor_triad(root_note,mode)
            elif chord_type == 'M7':
                notes = major_seventh(root_note,mode)
            elif chord_type == 'm7':
                notes = minor_seventh(root_note,mode)
            elif chord_type == '7':
                notes = dominant_seventh(root_note,mode)
            else:
                raise ValueError(f"Unknown chord type: {chord_type}")

            # Create a music21 chord object with these notes
            c = chord.Chord(notes, duration=duration.Duration(note_length))
            # Add the chord to the stream
            music_stream.append(c)

    # Once all the chords have been added to the stream, write the stream to a MIDI file
    
    filename = f"./result/{chord_name}chords_{mode}notes_{epoch}.mid"  # Construct the filename using f-string
    mf = midi.translate.streamToMidiFile(music_stream)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()






