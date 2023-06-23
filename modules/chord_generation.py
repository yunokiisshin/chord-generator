# chord_map_final.py: natural and varying voicing generator

from music21 import *
from music21.pitch import Pitch
import random

lowest_note = pitch.Pitch("F+3").midi
highest_note = pitch.Pitch("D4").midi

'''changes the sound by entering any given semitone number'''
def shift(note, semitones):
    p = Pitch(note)
    midi_num = p.midi + semitones
    return Pitch(midi_num).nameWithOctave



def chord_member(chord):
    