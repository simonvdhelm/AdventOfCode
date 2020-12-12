def eyr(value):
    return ((int(value) >= 2020) & (int(value) <= 2030))

def iyr(value):
    return ((int(value) >= 2010) & (int(value) <= 2020))

def hcl(value):
    if ((value[0] == "#") & (len(value) == 7)):
        try:
            color = int(value[1:],base=16)
            return True
        except ValueError:
            return False
    else:
        return False

def byr(value):
    return ((int(value) >= 1920) & (int(value) <= 2002))

def ecl(value):
    return (value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))

def hgt(value):
    try:
        height = int(value[:-2])
        if value[-2:] == "in":
            return ((height >= 59) & (height <= 76))
        elif value[-2:] == "cm":
            return ((height >= 150) & (height <= 193))
        else:
            return False
    except ValueError:
        return False


def pid(value):
    if len(value)==9:
        try:
            persId = int(value)
            return True
        except ValueError:
            return False
    else:
        return False

def cid(value):
    return True

def validKey(key,value):
    switcher = {
        "eyr": eyr,
        "iyr": iyr,
        "hcl": hcl,
        "byr": byr,
        "ecl": ecl,
        "hgt": hgt,
        "pid": pid,
        "cid": cid
    }
    func = switcher.get(key,lambda: True)
    return func(value)

if __name__ == '__main__':
    file = open('Input/Passports.txt','r')
    lines = file.readlines()

    entryCodes = ['eyr', 'iyr', 'hcl', 'byr', 'ecl', 'hgt', 'pid']
    correctCount = 0
    passport = {}

    for line in lines:
        if line != '\n':
            idx = []
            for i, c in enumerate(line):
                if c == ':':
                    idx.append(i)

            for i in range(len(idx)):
                key = line[idx[i]-3:idx[i]]
                if i < (len(idx)-1):
                    passport[key] = line[idx[i]+1:idx[i+1]-4]
                else:
                    passport[key] = line[idx[i]+1:-1]

        else:
            #print(passport.keys())
            if (all(validKey(key,value) for key,value in passport.items()) & all(key in passport for key in entryCodes)):
                correctCount+= 1
            passport = {}

    if (all(validKey(key,value) for key,value in passport.items()) & all(key in passport for key in entryCodes)):
        correctCount += 1

    print(correctCount)
