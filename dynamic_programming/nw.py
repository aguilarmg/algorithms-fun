from utils import readFile
from utils_nw import Alignment, extractData

# DATA_FILE='data/nw_00.txt'
# DATA_FILE='data/nw_01.txt'
DATA_FILE='data/nw_02.txt'

def main():
    nw_rawdata = readFile(DATA_FILE)
    (X, Y, a_gap, a_mm) = extractData(nw_rawdata) 
    print(f"X: {X}")
    print(f"Y: {Y}")
    print(f"gap cost: {a_gap}")
    print(f"mismatch cost: {a_mm}")
    seq_align = Alignment(X, Y, a_gap, a_mm)
    seq_align.fillGrid()
    nw_score = seq_align.getNWScore(len(X), len(Y))
    print(f"The NW score of this alignment is: {nw_score}")
    (aX, aY) = seq_align.constructAlignment()
    print(f"Aligned X: {aX}")
    print(f"Aligned Y: {aY}")

if __name__=='__main__':
    main()
