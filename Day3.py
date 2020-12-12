import numpy as np

if __name__ == '__main__':
    file = open('Input/Slope.txt','r')
    lines = file.readlines()

    indx = np.array([0, 0, 0, 0,0])
    count = np.array([0, 0, 0, 0,0])
    linecount = 0

    for line in lines:
        for ii in range(4):
            if line[indx[ii]] == '#':
                count[ii] = count[ii]+1
        if linecount % 2 == 0:
            if line[indx[4]] == '#':
                count[4] = count[4]+1
            indx[4] = (indx[4]+1)
        indx = (indx+[1, 3, 5, 7,0])%31
        linecount = linecount+1
    print(count)
    print(count.prod())