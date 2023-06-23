# Chord Progression Generator

This is an algorithm that creates a smooth but varying chord progression from given chord symbols.


## Requirements
- python 3+
- music21


## Usage
- Sample command line: python3 main.py "G Bm A Em" 10 3
- When asked for input, separate each bar by space and each beat by "/".
A valid input example is "C/C/C/G7 Am F/F/F/Em G"; currently supported chord symbols are none(major triad), m(minor triad), M7(major seventh), m7(minor seventh), 7(dominant seventh).
- Output will be saved in ./result folder with appropriate names.
