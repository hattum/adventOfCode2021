f = open("input.txt")
f = f.read()
fishes = [int(x) for x in f.split(',')]
week = [0,0,0,0,0,0,0]
totalNum = 0
for fish in fishes:
    week[fish] += 1
    totalNum += 1

days = 256

addToThis = 0
addToNext = 0
addToNextNext = 0

for day in range(days):
    weekDay = day%7
    temp = addToThis
    addToThis = addToNext
    addToNext = addToNextNext
    addToNextNext = week[weekDay]
    totalNum += week[weekDay]
    week[weekDay] += addToThis
print(totalNum)