#chord_to_midi.py: １小節１コード、リズムなしのシンプルなMIDI書き出し担当


from music21 import *
from modules.chord_map_custom import *
from modules.chord_map_final import *

def block_chords_to_midi(chord_symbols, epoch, mode):
    # Create a music21 stream object to hold the notes and chords
    music_stream = stream.Stream()    

    # create a dictionary
    progression = dict([("bar1", chord_symbols[0]), 
                        ("bar2", chord_symbols[1]), 
                        ("bar3", chord_symbols[2]), 
                        ("bar4", chord_symbols[3])])
    print(progression)
    
    
    chord_name = ''
    for bar in progression.values():
        bar_mod = bar.replace("/", "")
        print(bar)
        chord_name = chord_name + bar_mod + '_'
        if "/" in bar:
            chords_in_bar = bar.split('/') # "C/C/C/G" -> ['C', 'C', 'C', 'G']
        else: 
            chords_in_bar = [bar] # if there's only one chord in the bar, still make it a list

        for chord_symbol in chords_in_bar:
            # process chord_symbol as before

            # Determine the root note and the type of chord
            root_note = chord_symbol[0]
            if len(chord_symbol) > 1 and chord_symbol[1] in ["#", "b"]:
                root_note += chord_symbol[1]
                chord_type = chord_symbol[2:]
            else:
                chord_type = chord_symbol[1:]
            
            # Generate the notes for this chord
            notes = generate(root_note, chord_type, mode)

            # Create a music21 chord object with these notes
            
            note_length = 4.0 / len(chords_in_bar) # apply the shifting speed of in-bar chords

            c = chord.Chord(notes, duration=duration.Duration(note_length))
            # Add the chord to the stream
            music_stream.append(c)

    # Once all the chords have been added to the stream, write the stream to a MIDI file
    
    filename = f"./result/{chord_name}{mode}notes_{epoch}.mid"  # Construct the filename using f-string
    mf = midi.translate.streamToMidiFile(music_stream)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()