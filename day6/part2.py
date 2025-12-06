
with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

ops = lines.pop()

operation_list = []
starters_list = []
for char in ops:
    if char == '*':
        operation_list.append(lambda x, y : x * y)
        starters_list.append(1)
    elif char == '+':
        operation_list.append(lambda x, y : x + y)
        starters_list.append(0)

# Make everything an even matrix
max_line_length = 0
for i in range(len(lines)):
    max_line_length = max(max_line_length, len(lines[i]))
max_line_length += 1
for i in range(len(lines)):
    if len(lines) < max_line_length:
        for _ in range(max_line_length - len(lines[i])):
            lines[i] += ' '

vertical_numbers = []
column = 0
for j in range(max_line_length):
    has_num = False
    acc = 0
    for i in range(len(lines)):
        char = lines[i][:1]
        if char != ' ':
            digit = int(char)
            has_num = True
            acc = acc * 10 + digit
        lines[i] = lines[i][1:]

    if has_num:
        vertical_numbers.append(acc)
    else:
        for num in vertical_numbers:
            starters_list[column] = operation_list[column](starters_list[column], num)
        column += 1
        vertical_numbers = []

total = 0
for num in starters_list:
    total += num

print(total)



