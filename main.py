# main.py: description on code logics and algorithm

import sys
from modules.outdated.chord_map import *
from modules.chord_to_midi import *

'''
sample command line: python3 main.py "G Bm A Em" 10 3
Parameters:
    chord_symbols - input chord progression. 
    iter          - amount of variations to be generated. Each file will contain 4-bar progression.
    mode          - output mode. currently only support 3 for three-note generation.

Output: MIDI files of iter versions will be saved in ./output file. 

logics: 
The program looks at the middle note of the previous chord, and select the closest note 
to it in the current chord. It then chooses notes at most nine half-steps away from that note,
creating a relatively close but varying voicings
'''

def main(chord_symbols, iter, mode):
    
    # check if chord_symbols is a list
    if isinstance(chord_symbols, str):
        chord_symbols = chord_symbols.split()

    for epoch in range(1, iter+1):  
        block_chords_to_midi(chord_symbols, epoch, mode)

if __name__ == "__main__":
    # getting command line; example: python3 main.py "G Bm A Em" 10 3
    
    chord_symbols = sys.argv[1]  # the first argument after the script name
    iter = int(sys.argv[2]) 
    mode = int(sys.argv[3])
    main(chord_symbols, iter, mode)
