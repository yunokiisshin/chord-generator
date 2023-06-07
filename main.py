from chord_map import *
from chord_to_midi import *

def main():
    # Test with a simple chord progression
    chord_symbols = input("list chord progression: ").split()
    iter = int(input("How many iterations would you like?: "))
    print(chord_symbols)
    note_length = 4.0  # whole notes

    for epoch in range(1, iter+1):  
        block_chord_progression_to_midi(chord_symbols, note_length, epoch)

if __name__ == "__main__":
    main()