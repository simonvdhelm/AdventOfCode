if __name__ == '__main__':
    file = open('C:/Users/skorm/PycharmProjects/AdventOfCode/Day1/numbers.txt', 'r')
    Lines = file.readlines()

    count = 0
    numbers = []

    for line in Lines:
        numbers.append(int(line.strip()))

    for ii in range(len(numbers)):
        for jj in range(ii+1,len(numbers)):
            for kk in range(jj+1,len(numbers)):
                if (numbers[ii]+numbers[jj]+numbers[kk] == 2020):
                    product = numbers[ii]*numbers[jj]*numbers[kk]
                    break

    print(product)
