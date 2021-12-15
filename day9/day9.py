from typing import Callable


f = open("input.txt")
f = f.read()
grid = []
for line in f.split('\n'):
    numbers = []
    for num in line:
        numbers.append([int(num),True])
    grid.append(numbers)

def getValue(y,x):
    if x > len(grid[0])-1 or x<0 or y > len(grid)-1 or y< 0:
        return 10
    return grid[y][x][0]

def getBasin(y,x):
    if x > len(grid[0])-1 or x<0 or y > len(grid)-1 or y< 0:
        return False
    return grid[y][x][1]

def calculateBasin(y,x):
    global total
    grid[y][x][1] = False
    value = grid[y][x][0]
    # print(y,x)
    if 9>getValue(y+1,x)>value and getBasin(y+1,x):
        total +=1
        calculateBasin(y+1,x)
    if 9>getValue(y-1,x)>value and getBasin(y-1,x):
        total +=1
        calculateBasin(y-1,x)
    if 9>getValue(y,x+1)>value and getBasin(y,x+1):
        total +=1
        calculateBasin(y,x+1)
    if 9>getValue(y,x-1)>value and getBasin(y,x-1):
        total +=1
        calculateBasin(y,x-1)
    else:
        return


total = 0
basins = []
for j in range(len(grid)):
    length = len(grid[j])
    for i in range(length):
        isLowPoint = True
        value = grid[j][i][0]
        if getValue(j+1,i)<=value:
            isLowPoint = False
        elif getValue(j-1,i)<=value:
            isLowPoint = False
        elif getValue(j,i+1)<=value:
            isLowPoint = False
        elif getValue(j,i-1)<=value:
            isLowPoint = False
        if isLowPoint:
            total = 1
            calculateBasin(j,i)
            basins.append(total)
            total += value +1

basins = sorted(basins,reverse=True)
print(basins)
total = 1
for i in range(3):
    total = basins[i]*total

print(total)
    
# print(total)