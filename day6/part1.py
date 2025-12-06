
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

ops = lines.pop()

operation_list = []
accumulation_list = []
for char in ops:
    if char == '*':
        operation_list.append(lambda x, y : x * y)
        accumulation_list.append(1)
    elif char == '+':
        operation_list.append(lambda x, y : x + y)
        accumulation_list.append(0)

for line in lines:
    nums = line.split(' ')
    nums = [n for n in nums if n != '']
    for i in range(len(nums)):
        val = int(nums[i])
        accumulation_list[i] = operation_list[i](accumulation_list[i], val)

total = 0
for num in accumulation_list:
    total += num

print(total)



