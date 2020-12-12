import numpy as np

def getAdjacentSeats(seat,seats):
    N = range(seat[0]-1,seat[0]+2)
    M = range(seat[1]-1,seat[1]+2)
    x = []
    y = []
    for n in N:
        for m in M:
            if (not ((n == seat[0]) and (m == seat[1]))) and n >= 0 and n < seats.shape[0] and m >= 0 and m < seats.shape[1]:
                x.append(n)
                y.append(m)

    return tuple(x), tuple(y)

def getVisibleSeat(seat,seats,dir):
    dist = 1
    while not (seat[0] + dir[0] * dist < 0 or seat[0] + dir[0] * dist >= seats.shape[0]) and not (
            seat[1] + dir[1] * dist < 0 or seat[1] + dir[1] * dist >= seats.shape[1]):
        if not (seats[seat[0] + dir[0] * dist, seat[1] + dir[1] * dist] > 0):
            dist += 1
        else:
            return seat[0]+dir[0]*dist, seat[1]+dir[1]*dist

    return seat

def getVisibleSeats(seat,seats):
    dirX = (0, -1, -1, -1, 0, 1, 1, 1)
    dirY = (1, 1, 0, -1, -1, -1, 0, 1)

    x = []
    y = []

    for ii in range(8):
        tempX,tempY = getVisibleSeat(seat,seats,(dirX[ii],dirY[ii]))
        if not(tempX == seat[0] and tempY == seat[1]):
            x.append(tempX)
            y.append(tempY)

    return tuple(x), tuple(y)

def updateEmptySeat(seat, seats,seatFunc):
    adjSeats = seatFunc(seat,seats)
    if np.sum(seats[adjSeats]==2) == 0:
        return 2
    else:
        return 1


def updateTakenSeat(seat, seats,seatFunc):
    adjSeats = seatFunc(seat,seats)
    if (seatFunc == getVisibleSeats):
        occNeeded = 5
    else:
        occNeeded = 4
    if np.sum(seats[adjSeats]==2) >= occNeeded:
        return 1
    else:
        return 2

def updateFloor(seat, seats,seatFunc):
    return 0




def updateSeat(seat, seats,seatFunc):
    switcher = {
        0: updateFloor,
        1: updateEmptySeat,
        2: updateTakenSeat
    }
    func = switcher.get(seats[seat])
    return func(seat, seats,seatFunc)


if __name__ == "__main__":
    file = open("Input/Seatplan.txt")
    lines = file.readlines()

    seats = np.empty((len(lines),len(lines[1])-1), dtype=int)

    for (ii, line) in enumerate(lines):
        for (jj, c) in enumerate(line):
            if c == 'L':
                seats[ii][jj] = 1
            elif c == '.':
                seats[ii][jj] = 0

    changed = True

    while changed:
        newSeats = seats.copy()

        for ii in range(0,seats.shape[0]):
            for jj in range(0,seats.shape[1]):
                newSeats[ii,jj] = updateSeat((ii,jj),seats,getAdjacentSeats) #getAdjacentSeats for part 1, getVisibleSeats for part 2

        comp = newSeats != seats
        changed = np.any(comp)

        seats = newSeats

    print(np.sum(seats == 2))