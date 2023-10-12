import statistics

def median(x):
    if len(x) == 0:
        return 0
    solvedMedian = statistics.median(x)
    return solvedMedian

def mode(x):
    if len(x) == 0:
        return 0
    solvedMode = statistics.mode(x)
    return solvedMode

def mean(x):
    if len(x) == 0:
        return 0
    sum = 0
    for n in x:
        sum += n
    meanOfX = sum / len(x)
    return meanOfX

def main():
    lyst = [3, 1, 7, 1, 4, 10]
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median", median(lyst))   
    print("Mean:", mean(lyst))
    

main()
