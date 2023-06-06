# chord_map.py

from music21.pitch import Pitch

def note_shift(note, semitones):
    p = Pitch(note)
    midi_num = p.midi + semitones
    return Pitch(midi_num).nameWithOctave

def major_triad(root):
    return [root, note_shift(root, 4), note_shift(root, 7)]

def minor_triad(root):
    return [root, note_shift(root, 3), note_shift(root, 7)]

def major_seventh(root):
    return [root, note_shift(root, 4), note_shift(root, 7), note_shift(root, 11)]

def minor_seventh(root):
    return [root, note_shift(root, 3), note_shift(root, 7), note_shift(root, 10)]

def dominant_seventh(root):
    return [root, note_shift(root, 4), note_shift(root, 7), note_shift(root, 10)]
