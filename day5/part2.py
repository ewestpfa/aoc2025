
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

# I dislike python for loops :( - they don't behave the way I thought they did when the list length changes
i = 0
while i < len(valid_ranges):
    j = i + 1
    while j < len(valid_ranges):
        one = valid_ranges[i]
        two = valid_ranges[j]

        if one[0] <= two[0] <= one[1]:
            if two[1] <= one[1]:
                valid_ranges.pop(j)
                j -= 1
            else:
                valid_ranges[j] = (one[1] + 1, two[1])
        elif one[0] <= two[1] <= one[1]:
            valid_ranges[j] = (two[0], one[0] - 1)
        elif two[0] < one[0] and two[1] > one[1]:
            valid_ranges[j] = (two[0], one[0] - 1)
            valid_ranges.append((one[1] + 1, two[1]))

        j += 1
    i += 1

total = 0
for a_range in valid_ranges:
    if a_range != (-1, -1):
        total += a_range[1] - a_range[0] + 1

print(total)
