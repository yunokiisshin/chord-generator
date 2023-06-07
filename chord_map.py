from music21.pitch import Pitch
import random

def note_shift(note, semitones):
    p = Pitch(note)
    midi_num = p.midi + semitones
    return Pitch(midi_num).nameWithOctave

def major_triad(root):
    # Define the notes of the chord
    root_note = root
    third = note_shift(root_note, 4)
    fifth = note_shift(root_note, 7)

    # Define possible voicings
    voicings = [
        [root, third, fifth],            # root position
        [root, third, fifth, note_shift(root_note,12)], 
        [third, fifth, note_shift(root_note,12)],       # first inversion
        [third, fifth, note_shift(root_note,12), note_shift(third,12)],       # first inversion
        [note_shift(fifth, -12), root, third],  # second inversion
        [note_shift(fifth, -12), root, third, fifth],  # second inversion
        [root, fifth, note_shift(third,12), note_shift(fifth,12)]
        # Add more voicings as desired...
    ]

    # Randomly select a voicing
    voicing = random.choice(voicings)
    print(voicing)
    return voicing



def minor_triad(root):
    # Define the notes of the chord
    root_note = root
    third = note_shift(root_note, 3)
    fifth = note_shift(root_note, 7)

    # Define possible voicings
    voicings = [
        [root, third, fifth],       # root position
        [root, third, fifth, note_shift(root_note,12)], 
        [third, fifth, note_shift(root_note,12)],       # first inversion
        [third, fifth, note_shift(root_note,12), note_shift(third,12)],       # first inversion
        [note_shift(fifth, -12), root, third],  # second inversion
        [note_shift(fifth, -12), root, third, fifth],  # second inversion
        [root, fifth, note_shift(third,12), note_shift(fifth,12)]
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    voicing = random.choice(voicings)
    print(voicing)
    return voicing



def major_seventh(root):
     # Define the notes of the chord
    root_note = root
    third = note_shift(root_note, 4)
    fifth = note_shift(root_note, 7)
    seventh = note_shift(root_note,11)

    # Define possible voicings
    voicings = [
        [root, third, fifth, seventh],     # root position
        [root, fifth, seventh, note_shift(third,12)], 
        [root, seventh, note_shift(third,12), note_shift(fifth, 12)],  
        [third, fifth, seventh, note_shift(root_note, 12)],       # first inversion
        [third, seventh, note_shift(root_note, 12), note_shift(fifth, 12)],       
        [third, seventh, note_shift(root_note, 12), note_shift(fifth, 12)],       
        [note_shift(fifth, -12), note_shift(seventh, -12), root, third],  # second inversion
        [note_shift(fifth, -12), root, third, fifth], 
        [note_shift(seventh, -12), root, third, fifth]
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    voicing = random.choice(voicings)

    print(voicing)
    return voicing



def minor_seventh(root):
     # Define the notes of the chord
    root_note = root
    third = note_shift(root_note, 3)
    fifth = note_shift(root_note, 7)
    seventh = note_shift(root_note,10)

    # Define possible voicings
    voicings = [
        [root, third, fifth, seventh],     # root position
        [root, fifth, seventh, note_shift(third,12)], 
        [root, seventh, note_shift(third,12), note_shift(fifth, 12)],  
        [third, fifth, seventh, note_shift(root_note, 12)],       # first inversion
        [third, seventh, note_shift(root_note, 12), note_shift(fifth, 12)],       
        [third, seventh, note_shift(root_note, 12), note_shift(fifth, 12)],       
        [note_shift(fifth, -12), note_shift(seventh, -12), root, third],  # second inversion
        [note_shift(fifth, -12), root, third, fifth], 
        [note_shift(seventh, -12), root, third, fifth]
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    voicing = random.choice(voicings)
    print(voicing)
    return voicing


def dominant_seventh(root):
     # Define the notes of the chord
    root_note = root
    third = note_shift(root_note, 4)
    fifth = note_shift(root_note, 7)
    seventh = note_shift(root_note,10)

    # Define possible voicings
    voicings = [
        [root, third, fifth, seventh],     # root position
        [root, fifth, seventh, note_shift(third,12)], 
        [root, seventh, note_shift(third,12), note_shift(fifth, 12)],  
        [third, fifth, seventh, note_shift(root_note, 12)],       # first inversion
        [third, seventh, note_shift(root_note, 12), note_shift(fifth, 12)],       
        [third, seventh, note_shift(root_note, 12), note_shift(fifth, 12)],       
        [note_shift(fifth, -12), note_shift(seventh, -12), root, third],  # second inversion
        [note_shift(fifth, -12), root, third, fifth], 
        [note_shift(seventh, -12), root, third, fifth]
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    voicing = random.choice(voicings)
    print(voicing)

    return voicing
