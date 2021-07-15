lines_x_1 = []
lines_y_1 = []
lines_z_1 = []

def length1_line(i):
    i_base_x = i // 4
    i_base_y = i % 4
    layer = i // 16
    base_x = i_base_x * 4
    base_y = i_base_y + layer * 16
    base_z = i % 16
    lines_x_1.append((base_x, base_x+1, base_x+2, base_x+3))
    lines_y_1.append((base_y, base_y+4, base_y+8, base_y+12))
    lines_z_1.append((base_z, base_z+16, base_z+32, base_z+48))


for i in range(64):
    length1_line(i)

lines_x_1 = list(dict.fromkeys(lines_x_1))
lines_y_1 = list(dict.fromkeys(lines_y_1))
lines_z_1 = list(dict.fromkeys(lines_z_1))
print(lines_x_1)
print(lines_y_1)
print(lines_z_1)
