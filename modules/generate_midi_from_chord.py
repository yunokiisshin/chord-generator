#generate_midi_from_chord.py: wrapper function that writes out the MIDI file that contains input chord progressions

from music21 import *
from modules.outdated.chord_map_custom import *
from modules.chord_map_final import *

chord_history = {'symbol': None, 'notes': []}

def generate_midi_from_chord(chord_symbols, epoch, mode):
    # Create a music21 stream object to hold the notes and chords
    music_stream = stream.Stream()    
    previous_notes = []
    # create a dictionary
    progression = dict([("bar1", chord_symbols[0]), 
                        ("bar2", chord_symbols[1]), 
                        ("bar3", chord_symbols[2]), 
                        ("bar4", chord_symbols[3])])

    chord_name = ''
    for bar in progression.values():
        bar_mod = bar.replace("/", "")
        chord_name = chord_name + bar_mod + '_'
        if "/" in bar:
            chords_in_bar = bar.split('/') # "C/C/C/G" -> ['C', 'C', 'C', 'G']
        else: 
            chords_in_bar = [bar] # if there's only one chord in the bar, still make it a list

        for chord_symbol in chords_in_bar:
            
            # Determine the root note and the type of chord
            root_note = chord_symbol[0]
            if len(chord_symbol) == 1:
                chord_type = ''
            elif len(chord_symbol) > 1 and (chord_symbol[1] == "#" or chord_symbol[1] == "b"):
                root_note += chord_symbol[1]
                chord_type = chord_symbol[2:]
            else:
                chord_type = chord_symbol[1:]
            
        # If the chord is the same as the last one, use the same notes
            if chord_symbol == chord_history['symbol']:
                notes = chord_history['notes']
            else:  # Otherwise, generate new notes
                notes = generate(root_note, chord_type, mode, previous_notes)
                previous_notes.clear()
                previous_notes.extend(notes)

                # Update the chord history
                chord_history['symbol'] = chord_symbol
                chord_history['notes'] = notes

            
            note_length = 4.0 / len(chords_in_bar) # apply the shifting speed of in-bar chords
            c = chord.Chord(notes, duration=duration.Duration(note_length)) # Create a music21 chord object with these notes
            # Add the chord to the stream
            music_stream.append(c)

    # Once all the chords have been added to the stream, write the stream to a MIDI file
    filename = f"./result/{chord_name}{epoch}.mid"  # Construct the filename using f-string
    mf = midi.translate.streamToMidiFile(music_stream)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()