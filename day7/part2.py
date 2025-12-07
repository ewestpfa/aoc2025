
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

indices = [{}, {}]
count = 0
for i in range(len(lines)):
    if i % 2 == 0:
        indices[int(i/2) % 2] = {}
        if i == 0:
            for j in range(len(lines[i])):
                if lines[i][j:j+1] == 'S':
                    indices[i % 2][j] = 1

        else:
            for j in range(len(lines[i])):
                for val in indices[(int(i/2)+1) % 2].keys():
                    if j == val:
                        if lines[i][j:j+1] == '^':
                            if j-1 in indices[int(i/2) % 2].keys():
                                indices[int(i / 2) % 2][j-1] += indices[(int(i/2)+1) % 2][val]
                            else:
                                indices[int(i / 2) % 2][j - 1] = indices[(int(i / 2) + 1) % 2][val]
                            if j+1 in indices[int(i/2) % 2].keys():
                                indices[int(i / 2) % 2][j+1] += indices[(int(i/2)+1) % 2][val]
                            else:
                                indices[int(i / 2) % 2][j + 1] = indices[(int(i / 2) + 1) % 2][val]
                        else:
                            if val in indices[int(i/2) % 2].keys():
                                indices[int(i / 2) % 2][val] += indices[(int(i/2)+1) % 2][val]
                            else:
                                indices[int(i / 2) % 2][val] = indices[(int(i / 2) + 1) % 2][val]

            # print(indices[int(i / 2) % 2])

total = 0
for value in indices[(int(i/2)) % 2].values():
    total += value

print(total)

# 1683