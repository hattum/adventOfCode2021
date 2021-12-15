f = open("input.txt")
f = f.read()

data = f.split("\n\n")
drawNumbers = data.pop(0).split(',')
drawNumbers = [int(x) for x in drawNumbers]
# drawNumbers = [22,13]
# print(drawNumbers)
bordenLijst = []
for item in data:
    bord = []
    row = item.split('\n')
    for ding in row:
        getallen = ding.split(' ')
        ding = [int(x) for x in getallen if x!='']
        bord.append(ding)
    bordenLijst.append(bord)
    

def bordTotal(bord):
    total = 0
    for row in range(len(bordenLijst[0])):
        for col in range(len(bordenLijst[0][0])):
            if bordenLijst[bord][row][col] != -1:
                total += bordenLijst[bord][row][col]

    return(total)


def vinkNummber(n):
    for bord in range(len(bordenLijst)):
        for row in range(len(bordenLijst[0])):
            for col in range(len(bordenLijst[0][0])):
                if bordenLijst[bord][row][col] == n:
                    bordenLijst[bord][row][col] = -1

def checkWin():
    for bord in range(len(bordenLijst)):
        for row in range(len(bordenLijst[0])):
            rowWins = True
            for col in range(len(bordenLijst[0][0])):
                if bordenLijst[bord][row][col] != -1:
                    rowWins = False
            if rowWins:
                return(bord)
        for col in range(len(bordenLijst[0])):
            colWins = True
            for row in range(len(bordenLijst[0][0])):
                if bordenLijst[bord][row][col] != -1:
                    colWins = False
            if colWins:
                return(bord)
    return False

# Part 1

# winningBord = None
# lastVinkNumber = None
# while True:
#     winningBord = checkWin()
#     if winningBord:
#         print(winningBord)
#         break
#     # print(bordenLijst)
#     lastVinkNumber = drawNumbers.pop(0)
#     vinkNummber(lastVinkNumber)

lastVinkNumber = None
while len(bordenLijst)>1:
    # print(bordenLijst)
    while True:
        winningBord = checkWin()
        if winningBord is not False:
            bordenLijst.pop(winningBord)
        else:
            break
    lastVinkNumber = drawNumbers.pop(0)
    vinkNummber(lastVinkNumber)

while checkWin() is False:
    lastVinkNumber = drawNumbers.pop(0)
    vinkNummber(lastVinkNumber)
    
print(bordenLijst[0])

print(bordTotal(0))
print(bordTotal(0)*lastVinkNumber)
# print(bordTotal(winningBord)*lastVinkNumber)