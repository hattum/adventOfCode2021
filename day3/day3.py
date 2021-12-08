f = open("input.txt")
INPUT = []
temp = []

for l in f:
    l = l.strip()
    addList = []
    for i in range(len(l)):
        addList.append(int(l[i]))

    INPUT.append(addList)
    temp.append(addList)




for i in range(len(INPUT[0])):
    nrOnes = 0
    nrZero = 0
    nrList = len(INPUT)
    if nrList == 1:
        break
    for j in range(nrList):
        if INPUT[j][i] == 1:
            nrOnes +=1
        else:
            nrZero +=1

    needToDel = 0
    if nrZero > nrOnes:
        needToDel = 1
    j =0 
    while j<len(INPUT):
        if INPUT[j][i] == needToDel:
            INPUT.pop(j)
        else:
            j+=1
oxygen = INPUT[0]

INPUT = temp
for i in range(len(INPUT[0])):
    nrOnes = 0
    nrZero = 0
    nrList = len(INPUT)
    if nrList == 1:
        break
    for j in range(nrList):
        if INPUT[j][i] == 1:
            nrOnes +=1
        else:
            nrZero +=1

    needToDel = 0
    if nrZero <= nrOnes:
        needToDel = 1
    j =0 
    while j<len(INPUT):
        if INPUT[j][i] == needToDel:
            INPUT.pop(j)
        else:
            j+=1
scrubber = INPUT[0]
scrubber.reverse()
oxygen.reverse()
oxDec = 0
scrDec = 0
print(oxygen,scrubber)
for i in range(len(oxygen)):
    oxDec += 2**i*oxygen[i]
for i in range(len(scrubber)):
    scrDec += 2**i*scrubber[i]
# print(oxygen,INPUT)
# print(oxDec,scrDec)
print(oxDec*scrDec)