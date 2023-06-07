import sys
from chord_map import *
from chord_to_midi import *

'''
sample command line: main.py 'FM Dm CM CM' 4
Parameters:
    chord_symbols - 生成の際に指定するコード進行。1小節につき1コードを想定
                    M, m, M7, m7, 7のいずれかをコードの主音の後につけて入力(CM, Em7のように)
    iter          - 生成するファイル数。各ファイル毎に4小節のコード進行のバリエーションが保存される。

Output: resultフォルダにiterで指定した数のMIDIファイルが保存される。
'''
def main(chord_symbols, iter):
    
    # chord_symbolsがリストかの確認
    if isinstance(chord_symbols, str):
        chord_symbols = chord_symbols.split()
        
    note_length = 4.0  # コードは全音

    for epoch in range(1, iter+1):  
        block_chord_progression_to_midi(chord_symbols, note_length, epoch)

if __name__ == "__main__":
    # command lineの取得
    chord_symbols = sys.argv[1]  # the first argument after the script name
    iter = int(sys.argv[2])  # the second argument after the script name

    main(chord_symbols, iter)
