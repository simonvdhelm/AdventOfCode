ACCUMULATOR = 0
INDEX = 0


def acc(value):
    global ACCUMULATOR
    global INDEX

    ACCUMULATOR += value
    INDEX += 1


def jmp(value):
    global INDEX

    INDEX += value


def nop(value):
    global INDEX

    INDEX += 1


if __name__ == "__main__":
    file = open("Input/Instructions.txt", "r")
    lines = file.readlines()
    bInstruct = [False]*len(lines)

    for ii in range(len(lines)):
        instruct = lines[ii].split(' ')[0]

        if (instruct == "acc"):
            continue
        elif (instruct == "jmp"):
            lines[ii] = "nop" + lines[ii][3:]
        else:
            lines[ii] = "jmp" + lines[ii][3:]
        try:
            while True:
                if bInstruct[INDEX]:
                    break
                else:
                    bInstruct[INDEX] = True
                    function = lines[INDEX].split()
                    eval(function[0] + "(int(function[1]))")
        except IndexError:
            print(ACCUMULATOR)
            break

        lines[ii] = instruct + lines[ii][3:]
        INDEX = 0
        ACCUMULATOR = 0
        bInstruct = [False]*len(lines)

