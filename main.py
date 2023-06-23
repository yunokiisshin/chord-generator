# main.py: コード実行内容の記述

import sys
from modules.chord_map import *
from modules.chord_to_midi import *

'''
sample command line: python3 main.py "G Bm A Em" 10 3
Parameters:
    chord_symbols - input chord progression. 
    iter          - amount of variations to be generated. Each file will contain 4-bar progression.

Output: MIDI files of iter versions will be saved in ./output file. 

◯仕組みについて
コードシンボル毎に数種類のボイシングが用意してあり、ランダムで一つ選んで出力している。
そのため、プログラムが走るたびに違うバリエーションのコード進行が生成されるようになっている。

コード進行をリストに保存
→リストの要素ごとに、主音とコードに分け、それを元にコードのボイシングを返す。
→4つ返されたコードを一つのMIDIにまとめ、4小節のコード進行パターンとして保存する。
'''

def main(chord_symbols, iter, mode):
    
    # chord_symbolsがリストかの確認
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
