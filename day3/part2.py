
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

sum = 0
for line in lines:
    indexes = []
    while len(indexes) < 12:
        backups = []
        backup_max = 0
        max_val = 0
        max_idx = -1
        if len(indexes) == 0:
            for i in range(len(line)):
                num = int(line[i:i+1])
                if num > max_val:
                    max_val = num
                    max_idx = i
            indexes.append(max_idx)
            indexes.sort()
        else:
            found = False
            for j in range(len(indexes)-1, -1, -1):
                selected_idx = indexes[j]
                for i in range(selected_idx + 1, len(line)):
                    num = int(line[i:i+1])
                    if num > max_val and (i not in indexes):
                        max_val = num
                        max_idx = i
                if max_idx != -1:
                    indexes.append(max_idx)
                    indexes.sort()
                    found = True

                if found:
                    break

            if not found:
                for i in range(indexes[0]):
                    num = int(line[i:i + 1])
                    if num > max_val and (i not in indexes):
                        max_val = num
                        max_idx = i
                indexes.append(max_idx)
                indexes.sort()

    line_val = 0
    for idx in indexes:
        line_val = line_val * 10 + int(line[idx])

    sum += line_val
    print(line_val)

print(sum)