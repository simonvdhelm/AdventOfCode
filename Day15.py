def callNumber(lastCalled,count,calledNumbers):
    if lastCalled in calledNumbers:
        return count - calledNumbers[lastCalled]
    else:
        return 0

if __name__ == "__main__":
    file = open("Input/StartingNumbers.txt", "r")
    lines = file.readlines()

    for line in lines:
        numbers = [int(a) for a in line.split(',')]
        calledNumbers = {}

        for ii in range(len(numbers)-1):
            calledNumbers[numbers[ii]] = ii

        count = len(numbers)
        lastCalled = numbers[-1]
        while count < 30000000:
            newCalled = callNumber(lastCalled,count-1,calledNumbers)
            calledNumbers[lastCalled] = count-1
            count += 1
            lastCalled = newCalled

        print(newCalled)