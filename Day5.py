def findSeatID(boardingCode):
    rowStr = boardingCode[:7]
    colStr = boardingCode[7:]

    rowStr = rowStr.replace('F', '0')
    rowStr = rowStr.replace('B', '1')

    colStr = colStr.replace('L','0')
    colStr = colStr.replace('R','1')

    rowNr = int(rowStr,base=2)
    colNr = int(colStr,base=2)

    return rowNr*8+colNr

if __name__ == "__main__":
    file = open("Input/BoardingPasses.txt","r")
    lines = file.readlines()

    takenSeats = []

    for line in lines:
        takenSeats.append(findSeatID(line.strip()))

    takenSeats.sort()
    missingID = 0;

    for i in range(len(takenSeats)-1):
        if (takenSeats[i+1]-takenSeats[i] > 1):
            missingID = takenSeats[i]+1
            break

    print(missingID)