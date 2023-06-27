# chord_map_final.py: natural and varying voicing generator

from music21 import *
from music21.pitch import Pitch
import random

lowest_note = pitch.Pitch("F+3").midi
highest_note = pitch.Pitch("D4").midi

note_dict = dict([("root", []), ("third", []), ("fifth", [])])
 
'''changes the sound by entering any given semitone number'''
def shift(note, semitones):
    p = Pitch(note)
    midi_num = p.midi + semitones
    return Pitch(midi_num).nameWithOctave

'''fills up the value of dict's specified key'''
def fill_dict_value(note_dict, key, note):
    note_val = pitch.Pitch(note)
    while note_val.midi >= lowest_note:
        note_val.midi -= 12
        
    note_val.midi += 12
    while note_val.midi < highest_note:
        note_dict[key].append(note_val)
        note_val.midi += 12
        
    

def prepare_note_dict(root_note, chord_type):
    
    root = root_note.midi
    third = shift(root_note, )
    
    for dict_key in ["root", "third", "fifth"]:
        fill_dict_value(note_dict, dict_key, root)
        
    


def generate(root_note, chord_type, mode):
    
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
    
    



    return notes