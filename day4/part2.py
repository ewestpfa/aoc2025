
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
changed = True

while changed:
    changed = False
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "@" and count_adj(x, y) < 4:
                lines[y] = lines[y][:x] + "x" + lines[y][x+1:]
                total += 1
                changed = True

# Another idea is to programmatically accumulate which scrolls should be re-evaluated
# Every time a scroll is removed, add all adjacent scrolls to a list that needs to be re-evaluated
# Then just go through that list, adding adjacent scrolls as appropriate until the list is empty
# This might result in a slightly faster runtime on much larger boards

print(total)

