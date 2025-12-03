
with open("input.txt", "r") as f:
    i = f.read()

count = 0
valids = []
splits = i.split(",")
for item in splits:
    [start, end] = item.split("-")
    for num in range(int(start), int(end)+1):
        item = str(num)
        for sub_len in range(1, int(len(item) / 2)+1):
            invalid = False
            substrings = []
            for i in range(0, int(len(item)), sub_len):
                curr = item[i : i + sub_len]
                for j in range(len(substrings)):
                    if substrings[j] != curr:
                        invalid = True
                        continue
                substrings.append(curr)
            if not invalid and (num not in valids):
                valids.append(num)
                continue

for item in valids:
    count += item

print(count)