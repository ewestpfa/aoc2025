
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

sum = 0
for line in lines:
    max1 = 0
    max2 = 0
    idx1 = -1
    idx2 = -1
    for i in range(len(line)):
        num = int(line[i:i+1])
        if num > max1:
            max1 = num
            idx1 = i

    if idx1 == len(line) - 1: # if last digit is largest, find next largest for first digit
        max2 = max1
        max1 = 0
        idx2 = idx1
        idx1 = -1
        for i in range(len(line) - 1):
            num = int(line[i:i + 1])
            if num > max1:
                max1 = num
                idx1 = i
    else:
        for i in range(idx1 + 1, len(line)):
            num = int(line[i:i + 1])
            if num > max2:
                max2 = num
                idx2 = i

    sum += (max1 * 10 + max2)

print(sum)