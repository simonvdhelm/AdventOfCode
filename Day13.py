if __name__ == "__main__":
    file = open("Input/BusLines.txt", "r")
    lines = file.readlines()

    time = int(lines[0])
    busses = lines[1].split(",")
    busID = []
    offsets = []

    for ii, bus in enumerate(busses):
        if bus != "x":
            busID.append(int(bus))
            offsets.append(ii)

# PART ONE
    minWaitTime = min(busID)
    bestBus = minWaitTime
    for bus in busID:
        numRounds = time//bus
        waitTime = (bus*(numRounds+1))-time
        if waitTime < minWaitTime:
            minWaitTime = waitTime
            bestBus = bus

    print(minWaitTime*bestBus)

# PART TWO
    offset = 0
    period = busID[0]
    for ii in range(1,len(busID)):
        count = 0
        found = []
        while len(found)<2:
            count = count+1
            index = count*period+offset
            if (index+offsets[ii])%busID[ii] == 0:
                found.append(index)

        offset = found[0]
        period = found[1]-found[0]




    print(offset)
