
with open("input.txt", "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")

adj = [(i, j) for i in range(-1, 2, 1) for j in range(-1, 2, 1) if not (i == 0 and j == 0)]


def valid_idx(y: int, x: int):
    if y < 0:
        return False
    elif y >= len(lines):
        return False
    elif x < 0:
        return False
    elif x >= len(lines[y]):
        return False

    return True


def count_adj(x: int, y: int):
    count = 0
    for (xx, yy) in adj:

        if valid_idx(y+yy, x+xx) and lines[y + yy][x+xx] == "@":
            count += 1

    return count


total = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "@" and count_adj(x, y) < 4:
            total += 1

print(total)

