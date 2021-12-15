f = open("input.txt")
f = f.read()
grid = [[0]*1000 for j in range(1000)]

    
def addLine(start,end):
    if start[0] == end[0]:
        if start[1]>=end[1]:
            for i in range(end[1],start[1]+1,1):
                grid[i][start[0]] += 1
        else:
            for i in range(start[1],end[1]+1,1):
                # print(i)
                grid[i][start[0]] += 1

    elif start[1] == end[1]:
        if start[0] >= end[0]:
            for i in range(end[0],start[0]+1,1):
                # print(i)
                grid[start[1]][i] += 1
        else:
            for i in range(start[0],end[0]+1,1):
                # print(i)
                grid[start[1]][i] += 1
    else: 
        # 6,4 -> 2,0

        # 2 - 6
        # 0 - 4

        # 2,0
        # 3,1
        # 4,2
        # 5,3
        # 6,4  
        if start[0]>end[0] and start[1]>end[1]:
            for i in range(start[0]-end[0]+1):
                grid[end[1]+i][end[0]+i] += 1
        elif start[0]<end[0] and start[1]<end[1]:
            for i in range(end[0]-start[0]+1):
                grid[start[1]+i][start[0]+i] += 1
        #  [ 5,3 -> 3,5  ]
        elif start[0]>end[0] and start[1]<end[1]:
            for i in range(end[1]-start[1]+1):
                grid[end[1]-i][end[0]+i] += 1
        elif start[0]<end[0] and start[1]>end[1]:
            for i in range(end[0]-start[0]+1):
                grid[start[1]-i][start[0]+i] += 1



for line in f.split('\n'):
    line = line.split(" -> ")
    start = line[0].split(',')
    x = int(start[0])
    y = int(start[1])
    start = [x,y]

    end = line[1].split(',')
    x = int(end[0])
    y = int(end[1])
    end = [x,y]
    # print(start,end)
    addLine(start,end)
    # break

numOverlap = 0 
for col in grid:
    # print(col)
    for getal in col:
        if getal >= 2:
            numOverlap +=1
print(numOverlap)