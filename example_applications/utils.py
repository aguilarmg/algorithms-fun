from statistics import median

def foundIncorrectMedian(stream, x):
    return median(stream) != x

def genFrequencyMap(x):
    freqMap = {}
    for char in x:
        if char not in freqMap:
            freqMap[char] = 1
        else:
            freqMap[char] += 1
    for char in freqMap.keys():
        print(f"{char} -> {freqMap[char]}")

    return freqMap
