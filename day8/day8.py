from collections import Counter
f = open("input.txt")
f = f.read()
lines = f.split('\n')
total = 0


# for ding in lines[0].split(' | ')[0].split(' '):
#     if len(ding) == 2:
#         twee = ding
#     elif len(ding) == 4:
#         vier = ding

def easy(codes):
    for part in codes:
        if len(part) == 2:
            getallen[1] = part
        elif len(part) == 3:
            getallen[7] = part
        elif len(part) == 4:
            getallen[4] = part
        elif len(part) == 7:
            getallen[8] = part

def fives(codes):
    neededLetterFor5 = []
    neededLetterFor3 = []
    for letter in getallen[4]:
        if letter in getallen[1]:
            neededLetterFor3.append(letter)
        else:
            neededLetterFor5.append(letter)
    for code in codes:
        if len(code) == 5:
            if neededLetterFor5[0] in code and neededLetterFor5[1] in code:
                getallen[5] = code
            elif neededLetterFor3[0] in code and neededLetterFor3[1] in code:
                getallen[3] = code
            else:
                getallen[2] = code

def sixes(codes):
    for code in codes:
        if len(code) == 6:
            isNine = True
            isSix = True
            for letter in getallen[3]:
                if letter not in code:
                    isNine = False
            if getallen[1][0] in code and getallen[1][1] in code:
                isSix = False
            if isNine:
                getallen[9] = code
            elif isSix:
                getallen[6] = code
            else:
                getallen[0] = code


total = 0
for line in lines:
    firstCodes = line.split(' | ')[0].split(' ')
    lastCodes = line.split(' | ')[1].split(' ')
    getallen = [None,None,None,None,None,None,None,None,None,None]
    easy(firstCodes)
    fives(firstCodes)
    sixes(firstCodes)
    value = ''
    for code in lastCodes:
        for i in range(len(getallen)):
            if Counter(code) == Counter(getallen[i]):
                value = value+str(i)
                break

    total += int(value)
    
print(total)