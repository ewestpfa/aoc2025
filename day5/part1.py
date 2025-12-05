
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

valid_ranges = []
idx = 0
while lines[idx] != "":
    [low, high] = lines[idx].split("-")
    valid_ranges.append((int(low), int(high)))
    idx += 1

idx += 1

total = 0
while idx < len(lines):
    val = int(lines[idx])
    idx += 1
    for a_range in valid_ranges:
        if a_range[0] <= val <= a_range[1]:
            total += 1
            break

print(total)
