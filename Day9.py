def checkSum(idx, encVals, preamble=25):
    if idx >= preamble:
        for ii in range(idx-preamble, idx-1):
            for jj in range(ii+1, idx):
                if (encVals[ii]+encVals[jj]) == encVals[idx]:
                    return True
        return False
    else:
        return True

def findContiguousSet(idx,encVals):
    for ii in range(len(encVals)):
        contSum = 0
        count = 0
        while (contSum<encVals[idx]):
            contSum += encVals[ii+count]
            count += 1

        if contSum == encVals[idx]:
            return ii, ii+count



if __name__ == "__main__":
    file = open("Input/Encrypted.txt", "r")
    lines = file.readlines()
    encVals = []

    for line in lines:
        encVals.append(int(line))

    preamble = 25
    for ii in range(preamble, len(encVals)):
        if not checkSum(ii, encVals, preamble):
            break

    print(ii+1)
    print(encVals[ii])

    start, end = findContiguousSet(ii, encVals)
    minVal = min(encVals[start:end])
    maxVal = max(encVals[start:end])

    print(start)

    print(minVal+maxVal)