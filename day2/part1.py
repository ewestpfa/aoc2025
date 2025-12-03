
with open("input.txt", "r") as f:
    i = f.read()

count = 0
splits = i.split(",")
for item in splits:
    [start, end] = item.split("-")
    for num in range(int(start), int(end)+1):
        item = str(num)
        if len(item) % 2 == 0 and item != "":
            mid = int(len(item) / 2)
            if item[:mid] == item[mid:]:
                count += num

print(count)
