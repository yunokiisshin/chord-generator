from music21.pitch import Pitch
import random

def note_shift(note, semitones):
    p = Pitch(note)
    midi_num = p.midi + semitones
    return Pitch(midi_num).nameWithOctave

def major_triad(root):
    # Define the notes of the chord
    third = root + 4
    fifth = root + 7

    # Define possible voicings
    voicings = [
        [root, third, fifth],            # root position
        [root, third, fifth, root + 12], 
        [third, fifth, root + 12],       # first inversion
        [third, fifth, root + 12, third + 12],       # first inversion
        [fifth - 12, root, third],  # second inversion
        [fifth - 12, root, third, fifth],  # second inversion
        [root, fifth, third + 12, fifth + 12]
        # Add more voicings as desired...
    ]

    # Randomly select a voicing
    voicing = random.choice(voicings)
    return voicing

def minor_triad(root):
    # Define the notes of the chord
    third = root + 3
    fifth = root + 7

    # Define possible voicings
    voicings = [
        [root, third, fifth],            # root position
        [root, third, fifth, root + 12], 
        [third, fifth, root + 12],       # first inversion
        [third, fifth, root + 12, third + 12],       # first inversion
        [fifth - 12, root, third],  # second inversion
        [fifth - 12, root, third, fifth],  # second inversion
        [root, fifth, third + 12, fifth + 12]
        # Add more voicings as desired...
    ]


    # Randomly select a voicing
    voicing = random.choice(voicings)

    return voicing

def major_seventh(root):
    return [root, note_shift(root, 4), note_shift(root, 7), note_shift(root, 11)]

def minor_seventh(root):
    return [root, note_shift(root, 3), note_shift(root, 7), note_shift(root, 10)]

def dominant_seventh(root):
    return [root, note_shift(root, 4), note_shift(root, 7), note_shift(root, 10)]
