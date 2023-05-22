# Pattern searching using Boyer Moore algorithm
 
# Pre process 
def generateCharTable(pattern):
    chartable = [-1 for i in range (256)]
    pattern = str(pattern)
    for i in range (len(pattern)):
        chartable[ord(pattern[i])] = i
    return chartable
 
# Searching algorithm
def search(text, pattern):
    chartable = generateCharTable(pattern)
    
    m = len(pattern)
    n = len(text)
    s = 0

    while(s <= (n - m)):
        j = m - 1
 
        while (j >= 0 and pattern[j] == text[s + j]):
            j = j - 1
 
        if (j < 0):
            return s
        else:
            s += max(1, j - chartable[ord(text[s + j])])

    return -1
