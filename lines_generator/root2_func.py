lines_z_ullr = []
lines_z_urll = []
lines_x_bafo = []
lines_x_foba = []
lines_y_leri = []
lines_y_rile = []



def root2_line(i):
    layer = i // 16
    base = layer*16
    if i % 5 == layer:
        lines_z_ullr.append((base, base+5, base+10, base+15))
    if i % 4 + (i // 4) % 4 == 3:
        lines_z_urll.append((base+3, base+6, base+9, base+12))
    
    if (i - 16 * layer) // 4 == layer: 
        lines_x_bafo.append((i % 4, i % 4 + 20, i % 4 + 40, i % 4 + 60))
    if i % 12 == i % 4:
        lines_x_foba.append((i % 4 + 12, i % 4 + 12 + 12, i % 4 + 12 + 24, i % 4 + 12 + 36))

    if i % 4 == layer:
        lines_y_leri.append((i % 17, i % 17 + 17, i % 17 + 34, i % 17 + 51))
    if i % 4 + layer == 3:
        lines_y_rile.append((i % 15, i % 15 + 15, i % 15 + 30, i % 15 + 45))

for i in range(64):
    root2_line(i)

lines_z_ullr = list(dict.fromkeys(lines_z_ullr))
lines_z_urll = list(dict.fromkeys(lines_z_urll))
lines_x_bafo = list(dict.fromkeys(lines_x_bafo))
lines_x_foba = list(dict.fromkeys(lines_x_foba))
lines_y_leri = list(dict.fromkeys(lines_y_leri))
lines_y_rile = list(dict.fromkeys(lines_y_rile))

print(lines_z_ullr)
print(lines_z_urll)
print(lines_x_bafo)
print(lines_x_foba)
print(lines_y_leri)
print(lines_y_rile)