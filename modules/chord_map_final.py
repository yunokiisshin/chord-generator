# chord_map_final.py: natural and varying voicing generator
# only implementing triads

from music21 import *
from music21.pitch import Pitch
import random

lowest_note = pitch.Pitch("F#2").midi
highest_note = pitch.Pitch("D4").midi

note_dict = dict([("root", []), ("third", []), ("fifth", [])])
 
'''changes the sound by entering any given semitone number'''
def shift(note, semitones):
    midi_num = note.midi + semitones
    return Pitch(midi_num)

'''fills up the value of dict's specified key'''
def fill_dict_value(note_dict, key, note):
    note_val = note
    while note_val.midi >= lowest_note:
        note_val.midi -= 12
        
    note_val.midi += 12
    while note_val.midi <= highest_note:
        note_dict[key].append(note_val.midi)
        note_val.midi += 12
        

def prepare_note_dict(root_note, chord_type):
    root = root_note

    if chord_type == '':
        third = shift(root, 4)    
    elif chord_type == 'm':
        third = shift(root, 3)
    
    fifth = shift(root, 7)    

    fill_dict_value(note_dict, "root", root)
    fill_dict_value(note_dict, "third", third)
    fill_dict_value(note_dict, "fifth", fifth)

    print(note_dict)

    



def generate(root_note, chord_type, mode, previous_notes): # previous notes is list of pitch objects
    
    # convert previous_notes to int list
    previous_val = sorted(map(lambda x: x.midi, previous_notes))
    print(previous_val)

    # refresh the chord dictionary
    note_dict = dict([("root", []), ("third", []), ("fifth", [])])
    prepare_note_dict(root_note, chord_type)    
    
    # notes have to be a list of Pitch object
    notes = []
    
    # finding the middle note from previous chord as reference
    
    ref = previous_val[len(previous_val)/2]
    print(ref)
    
    # if this is the first time generating a chord
    if ref == '':
        root = random.choice(note_dict["root"])
        notes.append(root)
        third = random.choice(note_dict["third"])
        notes.append(third)
        fifth = random.choice(note_dict["fifth"])
        notes.append(fifth)
    
    else:
        note_list = sorted(note_dict.items())
        closest = note_list[0]
        distance = 100
        for i, note in enumerate(note_list):
            if abs(closest-note)<distance:
                closest = note_list[i]
                distance = abs(closest-note)
        
        first_note = closest
        notes.append(first_note)
        
        if first_note in note_dict["root"]:
            
        
            
        
    
    # find the closest note in the dictionary 
    
    
    return notes   



'''
def main():
    print(f"lowest value: {lowest_note}")
    print(f"highest value: {highest_note}")
    note = pitch.Pitch("G5")
    prepare_note_dict(note, '')

if __name__ == "__main__":
    main()
'''