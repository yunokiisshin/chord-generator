#chord_to_midi.py: １小節１コード、リズムなしのシンプルなMIDI書き出し担当


from music21 import *
from modules.chord_map_custom import *

def block_chords_to_midi(chord_symbols, epoch, mode):
    # Create a music21 stream object to hold the notes and chords
    music_stream = stream.Stream()    

    # create a dictionary
    progression = dict([("bar1", chord_symbols[0]), 
                        ("bar2", chord_symbols[1]), 
                        ("bar3", chord_symbols[2]), 
                        ("bar4", chord_symbols[3])])
    print(progression)
    
    for bar in progression.values():
        print(bar)
        if "/" in bar:
            bar.split('/') # "C/C/C/G" -> ['C', 'C', 'C', 'G']
        else: 
            list(bar)    
    
        for chord in bar:

            # Determine the root note and the type of chord
            root_note = chord[0]
            if chord[1] in ["#", "b"]:
                root_note += chord[1]
                chord_type = chord[2:]
            else:
                chord_type = chord[1:]
            
            # Generate the notes for the chord
            
            #balancing the sound range of chords
            root_note += "4"
            
            if chord_type == '':
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
            
            note_length = 4 / len(bar) # apply the shifting speed of in-bar chords
            c = chord.Chord(notes, duration=duration.Duration(note_length))
            # Add the chord to the stream
            music_stream.append(c)

    # Once all the chords have been added to the stream, write the stream to a MIDI file
    
    filename = f"./result/{chord_name}chords_{mode}notes_{epoch}.mid"  # Construct the filename using f-string
    mf = midi.translate.streamToMidiFile(music_stream)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()






