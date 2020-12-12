if __name__ == '__main__':
    file = open('Input/Passwords.txt', 'r')
    lines = file.readlines()

    count = 0

    for line in lines:
        indx = line.find('-')
        indy = line.find(' ')
        indz = line.find(':')

        minVal = int(line[0:indx])
        maxVal = int(line[indx+1:indy])
        letter = line[indy+1]

        if ((line[indz+1+minVal] == letter) ^ (line[indz+1+maxVal] == letter)):
            count = count+1

    print(count)