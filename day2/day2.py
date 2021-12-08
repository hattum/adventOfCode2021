f = open("input.txt")
horizontal = 0
depth = 0
aim = 0


for l in f:
    l = l.strip().split(" ")
    instruction = l[0]
    amount = int(l[1])
    if instruction == "forward":
        horizontal += amount
        depth += amount*aim
    elif instruction == "down":
        aim += amount
    elif instruction == "up":
        aim -= amount

print(horizontal*depth)