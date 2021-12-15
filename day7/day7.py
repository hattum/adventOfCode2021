f = open("input.txt")
f = f.read()
positions = [int(x) for x in f.split(',')]
# minPos = positions[0]
maxPos = positions[0]
for pos in positions:
    if pos>maxPos:
        maxPos = pos
    # if pos<minPos:
    #     minPos = pos
fuel = [0 for i in range(maxPos+1)]

for pos in positions:
    for i in range(len(fuel)):
        if i > pos:
            fuel[i] += (i-pos)*(i-pos+1)/2
        else:
            fuel[i] += (pos-i)*(pos-i+1)/2

minFuel = fuel[0]
for data in fuel:
    if data < minFuel:
        minFuel = data
print(minFuel)