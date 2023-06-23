# chord_map_final.py: natural and varying voicing generator

from music21 import *
from music21.pitch import Pitch
import random

lowest_note = pitch.Pitch("F+3").midi
highest_note = pitch.Pitch("D4").midi

note_dict = dict([("root", []), ("third", []), ("fifth", []), ("seventh", [])])

'''changes the sound by entering any given semitone number'''
def shift(note, semitones):
    p = Pitch(note)
    midi_num = p.midi + semitones
    return Pitch(midi_num).nameWithOctave



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