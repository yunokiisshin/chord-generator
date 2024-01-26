# Chord Progression Generator

This is an AI algorithm that creates a smooth but varying chord progression from given chord symbols.


## Requirements
- Python 3+
- music21

To run the program locally, first download or clone into the files so you can access them locally. Ensure you have Python environment.
On your terminal, run:
```
pip install music21
```

## Usage
- Sample command line: 
```
python3 main.py "G Bm A Em" 1 1
```
- When asked for input, separate each bar by space, and each beat by "/". A valid input example is "C/C/C/G7 Am F/F/F/Em G"; currently supported chord symbols are none(major triad), m(minor triad), M7(major seventh), m7(minor seventh), 7(dominant seventh). The following numbers are iteration (# of files of the same progression to generate) and mode (recommended: 1).
- Output will be saved in ./result folder with pre-assigned names.
 