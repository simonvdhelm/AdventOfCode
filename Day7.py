def findShinyGoldenBag(bag,codedBags):
    if "shinygold" in codedBags[bag]:
        return True

    elif "empty" in codedBags[bag]:
        return False

    else:
        return any(findShinyGoldenBag(contentBag, codedBags) for contentBag in codedBags[bag])

def findTotalNumberOfBags(bag,codedBags):
    if "empty" in codedBags[bag]:
        return 0

    else:
        numBags = 0
        for key in codedBags[bag]:
            numBags += (findTotalNumberOfBags(key, codedBags)+1)*codedBags[bag][key]
        return numBags


if __name__ == "__main__":
    file = open("Input/BagColors.txt", "r")
    lines = file.readlines()

    colorCoding = {}

    for line in lines:
         bag = line.split(' contain ')
         contents = bag[1].split(', ')
         bagCoding = {}

         for content in contents:
             try:
                words = content.split(' ')
                bagCoding[words[1]+words[2]] = int(words[0])
             except ValueError:
                 bagCoding["empty"] = True

         words = bag[0].split(' ')
         colorCoding[words[0]+words[1]] = bagCoding

    print(sum(findShinyGoldenBag(bags, colorCoding) for bags in colorCoding))
    print(findTotalNumberOfBags("shinygold", colorCoding))

