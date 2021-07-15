# all the list below stand for "start from top and end in bottom"

upper_left = []
upper_right = []
lower_left = []
lower_right = []


def root3_line(i):
    layer = i // 16
    if i % 4 == layer and (i - 16 * layer) // 4 == layer:
        upper_left.append((i % 21, i % 21 + 21, i % 21 + 42, i % 21 + 63))
    if i % 4 + layer == 3 and (i - 16 * layer) // 4 == layer:
        upper_right.append((i % 19, i % 19 + 19, i % 19 + 38, i % 19 + 57))
    if i % 4 == layer and (i - 16 * layer) // 4 + layer == 3:
        lower_left.append((i % 13, i % 13 + 13, i % 13 + 26, i % 13 + 39))
    if i % 4 + layer == 3 and (i - 16 * layer) // 4 + layer == 3:
        lower_right.append((i - 11 * layer, i - 11 * layer + 11, i - 11 * layer + 22, i - 11 * layer + 33))

for i in range(64):
    root3_line(i)


print(upper_left)
print(upper_right)
print(lower_left)
print(lower_right)