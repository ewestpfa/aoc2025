
with open("input.txt", "r") as f:
    lines = f.readlines()

pos = 50
count = 0
for line in lines:
    if line[0] == "L":
        direction = -1
    else:
        direction = 1

    distance = int(line[1:])
    for i in range(distance):
        pos = (pos + direction) % 100
        #part2
        if pos == 0:
            count += 1
            
    #part1
    # if pos == 0:
    #     count += 1

print(count)
