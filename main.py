# main.py: コード実行内容の記述

import sys
from modules.chord_map import *
from modules.chord_to_midi import *

'''
sample command line: main.py 'FM Dm CM CM' 4
Parameters:
    chord_symbols - 生成の際に指定するコード進行。1小節につき1コードを想定
                    M, m, M7, m7, 7のいずれかをコードの主音の後につけて入力(CM, Em7のように)
    iter          - 生成するファイル数。各ファイル毎に4小節のコード進行のバリエーションが保存される。

Output: resultフォルダにiterで指定した数のMIDIファイルが保存される。

◯仕組みについて
コードシンボル毎に数種類のボイシングを手入力で用意し、ランダムで一つ選んで出力している。
そのため、プログラムが走るたびに違うバリエーションのコード進行が生成されるようになっている。

コード進行をリストに保存
→リストの要素ごとに、主音とコードに分け、それを元にコードのボイシングを返す。
→4つ返されたコードを一つのMIDIにまとめ、4小節のコード進行パターンとして保存する。
'''
def main(chord_symbols, iter, mode):
    
    # chord_symbolsがリストかの確認
    if isinstance(chord_symbols, str):
        chord_symbols = chord_symbols.split()
        
    note_length = 4.0  # コードは全音

    for epoch in range(1, iter+1):  
        block_chords_to_midi(chord_symbols, note_length, epoch, mode)

if __name__ == "__main__":
    # command lineの取得
    chord_symbols = sys.argv[1]  # the first argument after the script name
    iter = int(sys.argv[2])  # the second argument after the script name
    mode = int(sys.argv[3])
    main(chord_symbols, iter, mode)
