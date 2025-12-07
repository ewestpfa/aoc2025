
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

indices = []
count = 0
for i in range(len(lines)):
    if i == 0:
        for j in range(len(lines[i])):
            if lines[i][j:j+1] == 'S':
                indices.append(j)

    else:
        for j in range(len(lines[i])):
            if lines[i][j:j+1] == '^' and j in indices:
                indices.remove(j)
                if j-1 not in indices:
                    indices.append(j-1)
                if j+1 not in indices:
                    indices.append(j+1)
                count += 1


print(count)

# 1683