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
     # Define the notes of the chord
    third = root + 4
    fifth = root + 7
    seventh = root + 11

    # Define possible voicings
    voicings = [
        [root, third, fifth, seventh],     # root position
        [root, fifth, seventh, third+12], 
        [root, seventh, third+12, fifth+12],  
        [third, fifth, seventh, root+12],       # first inversion
        [third, seventh, root+12, fifth+12],       
        [third, seventh, root+12, fifth+12],       
        [fifth - 12, seventh-12, root, third],  # second inversion
        [fifth - 12, root, third, fifth], 
        [seventh-12, root, third, fifth]
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    voicing = random.choice(voicings)

    return voicing



def minor_seventh(root):
     # Define the notes of the chord
    third = root + 3
    fifth = root + 7
    seventh = root + 10

    # Define possible voicings
    voicings = [
        [root, third, fifth, seventh],     # root position
        [root, fifth, seventh, third+12], 
        [root, seventh, third+12, fifth+12],  
        [third, fifth, seventh, root+12],       # first inversion
        [third, seventh, root+12, fifth+12],       
        [third, seventh, root+12, fifth+12],       
        [fifth - 12, seventh-12, root, third],  # second inversion
        [fifth - 12, root, third, fifth], 
        [seventh-12, root, third, fifth]
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    voicing = random.choice(voicings)

    return voicing



def dominant_seventh(root):
     # Define the notes of the chord
    third = root + 4
    fifth = root + 7
    seventh = root + 10

    # Define possible voicings
    voicings = [
        [root, third, fifth, seventh],     # root position
        [root, fifth, seventh, third+12], 
        [root, seventh, third+12, fifth+12],  
        [third, fifth, seventh, root+12],       # first inversion
        [third, seventh, root+12, fifth+12],       
        [third, seventh, root+12, fifth+12],       
        [fifth - 12, seventh-12, root, third],  # second inversion
        [fifth - 12, root, third, fifth], 
        [seventh-12, root, third, fifth]
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    voicing = random.choice(voicings)

    return voicing

