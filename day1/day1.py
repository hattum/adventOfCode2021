f = open("input.txt")
count = 0
lastThree = [int(f.readline()),int(f.readline()),int(f.readline())]


for l in f:
    lastSum = sum(lastThree)
    lastThree.pop(0)
    lastThree.append(int(l))
    if sum(lastThree)>lastSum:
        count+=1


print(count)

lijst = [2,3,4]
print(lijst.pop(0))