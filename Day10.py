import numpy as np

POSROUTES = None

def checkAdapters(start,end,adapters):
    global POSROUTES

    if POSROUTES[np.searchsorted(adapters,start)] != 0:
        return POSROUTES[np.searchsorted(adapters,start)]
    else:
        numWays = 0
        for ii in range(1, 4):
            if start+ii == end:
                numWays += 1
            elif np.searchsorted(adapters,start+ii,side='left') != np.searchsorted(adapters,start+ii,side='right'):
                numWays += checkAdapters(start+ii,end,adapters)

        POSROUTES[np.searchsorted(adapters,start)] = numWays
        return numWays

if __name__ == "__main__":
    file = open("Input/adapters.txt", "r")
    lines = file.readlines()

    adapters = np.array(lines, dtype='int64')

    adapters.sort()
    adapters = np.insert(adapters, 0, 0)
    adapters = np.append(adapters, np.amax(adapters)+3)

    joltInc = np.diff(adapters)

    print(np.count_nonzero(joltInc == 1)*np.count_nonzero(joltInc == 3))

    POSROUTES = [0]*len(adapters)
    print(checkAdapters(0,adapters[-1],adapters))

