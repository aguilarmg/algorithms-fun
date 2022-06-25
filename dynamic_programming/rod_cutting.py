from utils import readFile
from utils_rod import genCutPrices, calcOptRevenue

DATA_FILE='data/rod_00.txt'

def main():
    data = readFile(DATA_FILE)
    prices = genCutPrices(data)
    print(f"Prices: {prices}")
    n = len(prices)
    
    optRevenues = [None]*n
    
    for i in range(n):
        rev = calcOptRevenue(prices, optRevenues, i)
    for (l_i, rev) in enumerate(optRevenues):
        print(f"The opt revenue for a rod of length {l_i+1}: {rev}")

if __name__=='__main__':
    main()
