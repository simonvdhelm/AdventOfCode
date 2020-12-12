ORT = 0
XSHIP = 0
YSHIP = 0

XPOS = 10
YPOS = 1

def NorthOne(value):
    global YSHIP
    YSHIP += value


def EastOne(value):
    global XSHIP
    XSHIP += value


def SouthOne(value):
    global YSHIP
    YSHIP -= value


def WestOne(value):
    global XSHIP
    XSHIP -= value


def ForwardOne(value):
    global ORT
    switcher = {
        0: EastOne,
        1: NorthOne,
        2: WestOne,
        3: SouthOne
    }
    switcher.get(ORT)(value)

def LeftOne(value):
    global ORT

    ORT = (ORT+value/90) % 4


def RightOne(value):
    global ORT

    ORT = (ORT-value/90) % 4


def NorthTwo(value):
    global YPOS
    YPOS += value


def EastTwo(value):
    global XPOS
    XPOS += value


def SouthTwo(value):
    global YPOS
    YPOS -= value


def WestTwo(value):
    global XPOS
    XPOS -= value


def ForwardTwo(value):
    global XSHIP
    global YSHIP
    global XPOS
    global YPOS

    XSHIP += XPOS * value
    YSHIP += YPOS * value


def LeftTwo(value):
    global XPOS
    global YPOS

    for ii in range(int(value/90)):
        temp = XPOS
        XPOS = -YPOS
        YPOS = temp


def RightTwo(value):
    global XPOS
    global YPOS

    for ii in range(int(value / 90)):
        temp = XPOS
        XPOS = YPOS
        YPOS = -temp


if __name__ == "__main__":
    file = open("Input/BoatInstructions.txt", "r")
    lines = file.readlines()
    switcherOne = {
        "N": NorthOne,
        "E": EastOne,
        "S": SouthOne,
        "W": WestOne,
        "F": ForwardOne,
        "L": LeftOne,
        "R": RightOne
    }
    for line in lines:
        func = switcherOne.get(line[0])
        func(int(line[1:]))

    print(abs(XSHIP)+abs(YSHIP))

    XSHIP = 0
    YSHIP = 0

    switcherTwo = {
        "N": NorthTwo,
        "E": EastTwo,
        "S": SouthTwo,
        "W": WestTwo,
        "F": ForwardTwo,
        "L": LeftTwo,
        "R": RightTwo
    }

    for line in lines:
        switcherTwo.get(line[0])(int(line[1:]))

    print(abs(XSHIP)+abs(YSHIP))