# chord_map_custom.py: ボイシングを要綱に沿ってさらに指定したもの            

from music21 import *
from music21.pitch import Pitch
import random

'''changes the sound by entering any given semitone number'''
def shift(note, semitones):
    p = Pitch(note)
    midi_num = p.midi + semitones
    return Pitch(midi_num).nameWithOctave

'''changes the octaves randomly'''
def randomize_octave(note):
    p = Pitch(note)
    random_list = [-1,0,1,2]
    midi_num = p.midi + 12 * random.choice(random_list)
    return Pitch(midi_num).nameWithOctave



def major_triad(root,mode):
    # Define the notes of the chord
    root_note = root
    if Pitch(root_note).midi > 64: # higher than E4
        root_note = shift(root_note,-12) # F3-E4 is the root note range
    third = shift(root_note, 4)
    fifth = shift(root_note, 7)

    note_pool = [shift(third,-12), shift(fifth,-12),
                 root_note, third, fifth, 
                 shift(root_note,12), shift(third,12)]
    
    # Define possible voicings
    voicings = [
        [root, third, fifth],       # root position
        [third, fifth, shift(root_note,12)],       # first inversion
        [shift(fifth, -12), root, third],  # second inversion
        
        [root, third, fifth, shift(root_note,12)], 
        [third, fifth, shift(root_note,12), shift(third,12)],       # first inversion
        [fifth, shift(root_note,12), shift(third,12)],
        [shift(fifth, -12), root, third, fifth],  # second inversion
        [root, fifth, shift(third,12), shift(fifth,12)],
        
        [shift(root_note,-24), shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note],
        [shift(root_note,-24), shift(root_note,-12), shift(fifth,-12), root_note, third],
        [shift(third,-24), shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note],
        [shift(third,-24), shift(root_note,-12), shift(fifth,-12), root_note, third],
        [shift(fifth,-24), shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note],
        [shift(fifth,-24), shift(root_note,-12), shift(fifth,-12), root_note, third],
        [shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note, third],
        [shift(root_note,-12), shift(fifth,-12), root_note, third, fifth],
        
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    if mode==0:
        voicing = random.choice(voicings)
        return voicing
    
    elif mode==3:
        
        voicing = random.choice(voicings[0:3])
        return voicing

    elif mode == 5:
        voicing = random.choice(voicings[8:])
        return voicing
    



def minor_triad(root,mode):
    # Define the notes of the chord
    root_note = root
    if Pitch(root_note).midi > 64: # higher than E4
        root_note = shift(root_note,-12) # F3-E4 is the root note range
    third = shift(root_note, 3)
    fifth = shift(root_note, 7)

    note_pool = [shift(root_note,-12), shift(fifth,-12),
                 root_note, third, fifth, 
                 shift(root_note,12), shift(third,12), shift(fifth,12)]
    
    # Define possible voicings
    voicings = [
        [root, third, fifth],       # root position
        [third, fifth, shift(root_note,12)],       # first inversion
        [shift(fifth, -12), root, third],  # second inversion
        
        [root, third, fifth, shift(root_note,12)], 
        [third, fifth, shift(root_note,12), shift(third,12)],       # first inversion
        [shift(fifth, -12), root, third, fifth],  # second inversion
        [root, fifth, shift(third,12), shift(fifth,12)],
        
        [shift(root_note,-24), shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note],
        [shift(root_note,-24), shift(root_note,-12), shift(fifth,-12), root_note, third],
        [shift(third,-24), shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note],
        [shift(third,-24), shift(root_note,-12), shift(fifth,-12), root_note, third],
        [fifth, shift(root_note,12), shift(third,12)],
        [shift(fifth,-24), shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note],
        [shift(fifth,-24), shift(root_note,-12), shift(fifth,-12), root_note, third],
        [shift(root_note,-12), shift(third,-12), shift(fifth,-12), root_note, third],
        [shift(root_note,-12), shift(fifth,-12), root_note, third, fifth],
        
    ]
    
    # Randomly select a voicing
    if mode==0:
        voicing = random.choice(voicings)
        return voicing
    
    elif mode==3:
        
        voicing = random.choice(voicings[0:3])
        return voicing

    elif mode == 5:
        voicing = random.choice(voicings[8:])
        return voicing

    
    

def major_seventh(root,mode):
     # Define the notes of the chord
    root_note = root
    if Pitch(root_note).midi > 64: # higher than E4
        root_note = shift(root_note,12) # F3-E4 is the root note range
    third = shift(root_note, 4)
    fifth = shift(root_note, 7)
    seventh = shift(root_note,11)

    note_pool = [shift(seventh, -24),shift(root_note,-12), shift(fifth,-12),shift(seventh, -12),
                 root_note, third, fifth, seventh,
                 shift(root_note,12), shift(third,12), shift(fifth,12),shift(seventh, 12),
                 shift(root_note,24)]
    # Define possible voicings
    voicings = [
        [root_note, third, fifth, seventh],     # root position
        [root_note, third, shift(fifth,-12), seventh],     # root position
        [root_note, fifth, seventh, shift(third,12)], 
        [root_note, seventh, shift(third,12), shift(fifth, 12)],  
        [third, fifth, seventh, shift(root_note, 12)],       # first inversion
        [third, seventh, shift(root_note, 12), shift(fifth, 12)],       
        [third, seventh, shift(root_note, 12), shift(fifth, 12)],       
        [shift(fifth, -12), shift(seventh, -12), root_note, third],  # second inversion
        [shift(fifth, -12), root_note, third, fifth], 
        [shift(seventh, -12), root_note, third, fifth],
        
        [shift(root_note,-12), shift(third,-12), shift(seventh,-12), third],
        [shift(root_note,-12), shift(fifth,-12), shift(seventh,-12), root_note, third],
        [shift(root_note,-12),root_note, third, fifth, seventh],
        [shift(root_note,-12),root_note, third, fifth, shift(seventh,-12)],
        [shift(root_note,-12),root_note, third, shift(fifth,-12), shift(seventh,-12)],
        [shift(root_note,-12), third, fifth, shift(fifth,-12), shift(seventh,-12)],
        [shift(root_note,-24), shift(root_note,-12), shift(fifth,-12),shift(seventh,-12),third],
        [shift(root_note,-24), shift(root_note,-12), fifth, shift(seventh,-12),third],
        
        
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    if mode==0:
        voicing = random.choice(voicings)
        return voicing
    
    elif mode==3:
        
        voicing = random.choice(voicings[0:11])
        return voicing

    elif mode == 5:
        voicing = random.choice(voicings[11:])
        return voicing
    



def minor_seventh(root,mode):
     # Define the notes of the chord
    root_note = root 
    if Pitch(root_note).midi > 64: # higher than E4
        root_note = shift(root_note,12) # F3-E4 is the root note range
    third = shift(root_note, 3)
    fifth = shift(root_note, 7)
    seventh = shift(root_note,10)

    note_pool = [shift(seventh,-24),shift(root_note,-12), shift(fifth,-12),shift(seventh, -12),
                 root_note, third, fifth, seventh,
                 shift(root_note,12), shift(third,12), shift(fifth,12),shift(seventh, 12),
                 shift(root_note,24)]
    # Define possible voicings
    voicings = [
        [root_note, third, fifth, seventh],     # root position
        [root_note, third, shift(fifth,-12), seventh],     # root position
        [root_note, fifth, seventh, shift(third,12)], 
        [root_note, seventh, shift(third,12), shift(fifth, 12)],  
        [third, fifth, seventh, shift(root_note, 12)],       # first inversion
        [third, seventh, shift(root_note, 12), shift(fifth, 12)],       
        [third, seventh, shift(root_note, 12), shift(fifth, 12)],       
        [shift(fifth, -12), shift(seventh, -12), root_note, third],  # second inversion
        [shift(fifth, -12), root_note, third, fifth], 
        [shift(seventh, -12), root_note, third, fifth],
        
        [shift(root_note,-12), shift(third,-12), shift(seventh,-12), third],
        [shift(root_note,-12), shift(fifth,-12), shift(seventh,-12), root_note, third],
        [shift(root_note,-12),root_note, third, fifth, seventh],
        [shift(root_note,-12),root_note, third, fifth, shift(seventh,-12)],
        [shift(root_note,-12),root_note, third, shift(fifth,-12), shift(seventh,-12)],
        [shift(root_note,-12), third, fifth, shift(fifth,-12), shift(seventh,-12)],
        [shift(root_note,-24), shift(root_note,-12), shift(fifth,-12),shift(seventh,-12),third],
        [shift(root_note,-24), shift(root_note,-12), fifth, shift(seventh,-12),third],
        
        
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    if mode==0:
        voicing = random.choice(voicings)
        return voicing
    
    elif mode==3:
        
        voicing = random.choice(voicings[0:11])
        return voicing

    elif mode == 5:
        voicing = random.choice(voicings[11:])
        return voicing
    

def dominant_seventh(root,mode):
     # Define the notes of the chord
    root_note = root
    if Pitch(root_note).midi > 64: # higher than E4
        root_note = shift(root_note,12) # F3-E4 is the root note range
    third = shift(root_note, 4)
    fifth = shift(root_note, 7)
    seventh = shift(root_note,10)


    note_pool = [shift(root_note,-12), shift(fifth,-12),shift(seventh, -12),
                 root_note, third, fifth, seventh,
                 shift(root_note,12), shift(third,12), shift(fifth,12),shift(seventh, 12),
                 shift(root_note,24)]
    # Define possible voicings
    voicings = [
        [root_note, third, fifth, seventh],     # root position
        [root_note, third, shift(fifth,-12), seventh],     # root position
        [root_note, fifth, seventh, shift(third,12)], 
        [root_note, seventh, shift(third,12), shift(fifth, 12)],  
        [third, fifth, seventh, shift(root_note, 12)],       # first inversion
        [third, seventh, shift(root_note, 12), shift(fifth, 12)],       
        [third, seventh, shift(root_note, 12), shift(fifth, 12)],       
        [shift(fifth, -12), shift(seventh, -12), root_note, third],  # second inversion
        [shift(fifth, -12), root_note, third, fifth], 
        [shift(seventh, -12), root_note, third, fifth],
        
        [shift(root_note,-12), shift(third,-12), shift(seventh,-12), third],
        [shift(root_note,-12), shift(fifth,-12), shift(seventh,-12), root_note, third],
        [shift(root_note,-12),root_note, third, fifth, seventh],
        [shift(root_note,-12),root_note, third, fifth, shift(seventh,-12)],
        [shift(root_note,-12),root_note, third, shift(fifth,-12), shift(seventh,-12)],
        [shift(root_note,-12), third, fifth, shift(fifth,-12), shift(seventh,-12)],
        [shift(root_note,-24), shift(root_note,-12), shift(fifth,-12),shift(seventh,-12),third],
        [shift(root_note,-24), shift(root_note,-12), fifth, shift(seventh,-12),third],
        
        
        # Add more voicings as desired...
    ]
    
    # Randomly select a voicing
    if mode==0:
        voicing = random.choice(voicings)
        return voicing
    
    elif mode==3:
        
        voicing = random.choice(voicings[0:11])
        return voicing

    elif mode == 5:
        voicing = random.choice(voicings[11:])
        return voicing
    