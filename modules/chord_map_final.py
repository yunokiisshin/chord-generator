# chord_map_final.py: natural and varying voicing generator
# only implementing triads

from music21 import *
from music21.pitch import Pitch
import random

# variable to set the range of overall voicing
lowest_note = pitch.Pitch("F#3").midi
highest_note = pitch.Pitch("D5").midi

# dictionary container for each note for the processed chord
# contains ints that represent MIDI note value
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
        

'''fills up the entire note_dict'''
def prepare_note_dict(root_note, chord_type):
    root = Pitch(root_note)

    if chord_type == '':
        third = shift(root, 4)
    elif chord_type == 'm':
        third = shift(root, 3)

    fifth = shift(root, 7)

    fill_dict_value(note_dict, "root", root)
    fill_dict_value(note_dict, "third", third)
    fill_dict_value(note_dict, "fifth", fifth)


    
'''generate the current chord based on the previous input'''
def generate(root_note, chord_type, mode, previous_notes): # previous notes is list of pitch objects
    
    # convert previous_notes to int list
    previous_val = []
    for note in previous_notes:
        previous_val.append(note.midi)
    previous_val = sorted(previous_val)

    # clear the chord dictionary
    for key in note_dict.keys():
        note_dict[key].clear()
        
    prepare_note_dict(root_note, chord_type)   
     
    # notes have to be a list of Pitch object
    notes = []
    
    # if this is the first time generating a chord
    if previous_val == []:
        note_list = []
        for value in note_dict.values():
            for item in value:
                note_list.append(item)
        
        first_note = random.choice(note_list)
        notes.append(first_note)
        
        if first_note in note_dict["root"]: # choosing third and fifth
            bucket = []
            for item in note_dict["third"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            second_note = random.choice(bucket)
            notes.append(second_note)
            
            bucket.clear()
            for item in note_dict["fifth"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            third_note = random.choice(bucket)
            notes.append(third_note)
            
        elif first_note in note_dict["third"]: # choosing root and fifth
            bucket = []
            for item in note_dict["root"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            second_note = random.choice(bucket)
            notes.append(second_note)
            
            bucket.clear()
            for item in note_dict["fifth"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            third_note = random.choice(bucket)
            notes.append(third_note)
            
        elif first_note in note_dict["fifth"]: # choosing root and third
            bucket = []
            for item in note_dict["root"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            second_note = random.choice(bucket)
            notes.append(second_note)
            
            bucket.clear()
            for item in note_dict["third"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            third_note = random.choice(bucket)
            notes.append(third_note)

    else:   # there is a previous chord generated
        
        # finding the middle note from previous chord as reference
        ref = previous_val[len(previous_val)//2]
    
        
        note_list = []
        for value in note_dict.values():
            for item in value:
                note_list.append(item)
        closest = note_list[0]
        distance = 100
        for i, note in enumerate(note_list):
            if abs(ref - note) < distance:
                closest = note_list[i]
                distance = abs(closest-note)
        # make that note the first note of the current chord
        first_note = closest
        notes.append(first_note)
        
        if first_note in note_dict["root"]: # choosing third and fifth
            bucket = []
            for item in note_dict["third"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            second_note = random.choice(bucket)
            notes.append(second_note)
            
            bucket.clear()
            for item in note_dict["fifth"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            third_note = random.choice(bucket)
            notes.append(third_note)
            
        elif first_note in note_dict["third"]: # choosing root and fifth
            bucket = []
            for item in note_dict["root"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            second_note = random.choice(bucket)
            notes.append(second_note)
            
            bucket.clear()
            for item in note_dict["fifth"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            third_note = random.choice(bucket)
            notes.append(third_note)
            
        elif first_note in note_dict["fifth"]: # choosing root and third
            bucket = []
            for item in note_dict["root"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            second_note = random.choice(bucket)
            notes.append(second_note)
            
            bucket.clear()
            for item in note_dict["third"]:
                if abs(item-first_note) <= 9:
                    bucket.append(item)
            third_note = random.choice(bucket)
            notes.append(third_note)        
            
    note_pitches = []  
            
    for note in notes:
        midi_number = note
        p = pitch.Pitch()
        p.midi = midi_number
        note_pitches.append(p)
    
    return note_pitches


'''
def main():
    print(f"lowest value: {lowest_note}")
    print(f"highest value: {highest_note}")
    note = pitch.Pitch("G5")
    prepare_note_dict(note, '')

if __name__ == "__main__":
    main()
'''