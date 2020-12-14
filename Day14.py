MEM = {}

def applyMask(value, mask):
    binVal = list('{0:036b}'.format(value))
    for ii in range(len(mask)):
        if mask[ii] != 'X':
            binVal[ii] = mask[ii]

    returnVal = ""
    return (int(returnVal.join(binVal),base=2))

def applyMemoryMask(address, mask):
    global MEM
    binAddr = list('{0:036b}'.format(address))
    floating = []
    for ii in range(len(mask)):
        if mask[ii] == '1':
            binAddr[ii] = '1'
        elif mask[ii] == 'X':
            binAddr[ii] = '0'
            floating.append(ii)

    binAddrs = []
    for ii in range(2**len(floating)):
        binAddrs.append(binAddr.copy())

    step = 2
    for ii in range(len(floating)):
        for jj in range(0,len(binAddrs),step):
            for kk in range(jj,jj+int(step/2)):
                binAddrs[kk][floating[ii]] = '1'

        step = step*2

    returnVal = ""
    returnArray = []

    for binAddr in binAddrs:
        returnArray.append(int(returnVal.join(binAddr),base=2))

    return returnArray

if __name__ == "__main__":
    file = open("Input/DockingData.txt","r")
    lines = file.readlines()

    mask = None

    for line in lines:
        if line[1] == "a":
            mask = list(line.split(' ')[-1][0:-1])

        else:
            addr = line.split(']')[0].split('[')[1]
            value = int(line.split(' = ')[1])
            MEM[addr] = applyMask(value, mask)

    print(sum(MEM.values()))

    MEM = {}
    mask = None

    for line in lines:
        if line[1] == "a":
            mask = list(line.split(' ')[-1][0:-1])
        else:
            addr = int(line.split(']')[0].split('[')[1])
            value = int(line.split(' = ')[1])
            addr = applyMemoryMask(addr, mask)
            for ad in addr:
                MEM[ad] = value

    print(sum(MEM.values()))