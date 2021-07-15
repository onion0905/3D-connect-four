import pygame
import math
pygame.init()

# Screen
wn = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D connect-four")
icon = pygame.image.load("images/black_piece.png")
pygame.display.set_icon(icon)


# background
background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, (800, 600))
wn.blit(background, (0, 0))

# pieces
blue_piece = pygame.image.load("images/blue_piece.png")
blue_piece = pygame.transform.scale(blue_piece, (30, 30))
blue_piece.convert()
black_piece = pygame.image.load("images/black_piece.png")
black_piece = pygame.transform.scale(black_piece, (30, 30))
black_piece.convert()
white_piece = pygame.image.load("images/white_piece.png")
white_piece = pygame.transform.scale(white_piece, (30, 30))
white_piece.convert()
red_piece = pygame.image.load("images/red_piece.png")
red_piece = pygame.transform.scale(red_piece, (30, 30))
red_piece.convert()

# showing pieces
show = "all"
show_number = 1

# blocks
block_state = []
lock = []
block_coordinate = [(349, 65), (392, 64), (439, 64), (483, 64), (340, 95), (390, 95), (440, 95), (490, 95),\
                    (330, 126), (387, 126), (444, 126), (499, 126), (321, 160), (384, 160), (448, 160), (510, 160),\
                    (351, 200), (395, 200), (440, 200), (483, 200), (342, 232), (391, 232), (443, 232), (491, 232),\
                    (332, 264), (389, 264), (446, 264), (501, 264), (322, 297), (385, 297), (449, 297), (510, 297),\
                    (349, 339), (394, 339), (439, 339), (482, 339), (340, 371), (390, 371), (442, 371), (491, 371),\
                    (332, 402), (388, 402), (445, 402), (501, 402), (321, 435), (387, 435), (449, 437), (509, 437),\
                    (348, 473), (391, 473), (437, 473), (481, 473), (340, 504), (389, 504), (441, 504), (489, 504),\
                    (331, 535), (387, 535), (443, 533), (499, 533), (322, 570), (387, 570), (447, 570), (509, 570)]
for i in range(len(block_coordinate)):
    block_state.append("blue")
    lock.append(False)

color = "black"
color_coordinate = (156, 389)


# lines
# black lines
lines_x_1_black = []  # ----
lines_y_1_black = []  # /
lines_z_1_black = []  # |

lines_z_ullr_black = []
lines_z_urll_black = []
lines_x_bafo_black = []
lines_x_foba_black = []
lines_y_leri_black = []
lines_y_rile_black = []

upper_left_black = []
upper_right_black = []
lower_left_black = []
lower_right_black = []

# white lines
lines_x_1_white = []  # ----
lines_y_1_white = []  # /
lines_z_1_white = []  # |

lines_z_ullr_white = []
lines_z_urll_white = []
lines_x_bafo_white = []
lines_x_foba_white = []
lines_y_leri_white = []
lines_y_rile_white = []

upper_left_white = []
upper_right_white = []
lower_left_white = []
lower_right_white = []

winning_line = ()


# functions


def line_black(i):
    # length = 1 lines
    i_base_x = i // 4
    i_base_y = i % 4
    layer = i // 16
    base_x = i_base_x * 4
    base_y = i_base_y + layer * 16
    base_z = i % 16
    lines_x_1_black.append((base_x, base_x+1, base_x+2, base_x+3))
    lines_y_1_black.append((base_y, base_y+4, base_y+8, base_y+12))
    lines_z_1_black.append((base_z, base_z+16, base_z+32, base_z+48))
    # length = root 2 lines
    base = layer * 16
    if i % 5 == layer:
        lines_z_ullr_black.append((base, base + 5, base + 10, base + 15))
    if i % 4 + (i // 4) % 4 == 3:
        lines_z_urll_black.append((base + 3, base + 6, base + 9, base + 12))

    if (i - 16 * layer) // 4 == layer:
        lines_x_bafo_black.append((i % 4, i % 4 + 20, i % 4 + 40, i % 4 + 60))
    if i % 12 == i % 4:
        lines_x_foba_black.append((i % 4 + 12, i % 4 + 12 + 12, i % 4 + 12 + 24, i % 4 + 12 + 36))

    if i % 4 == layer:
        lines_y_leri_black.append((i % 17, i % 17 + 17, i % 17 + 34, i % 17 + 51))
    if i % 4 + layer == 3:
        lines_y_rile_black.append((i % 15, i % 15 + 15, i % 15 + 30, i % 15 + 45))
    # length = root 3 lines
    if i % 4 == layer and (i - 16 * layer) // 4 == layer:
        upper_left_black.append((i % 21, i % 21 + 21, i % 21 + 42, i % 21 + 63))
    if i % 4 + layer == 3 and (i - 16 * layer) // 4 == layer:
        upper_right_black.append((i % 19, i % 19 + 19, i % 19 + 38, i % 19 + 57))
    if i % 4 == layer and (i - 16 * layer) // 4 + layer == 3:
        lower_left_black.append((i % 13, i % 13 + 13, i % 13 + 26, i % 13 + 39))
    if i % 4 + layer == 3 and (i - 16 * layer) // 4 + layer == 3:
        lower_right_black.append((i - 11 * layer, i - 11 * layer + 11, i - 11 * layer + 22, i - 11 * layer + 33))


def line_white(i):
    # length = 1 lines
    i_base_x = i // 4
    i_base_y = i % 4
    layer = i // 16
    base_x = i_base_x * 4
    base_y = i_base_y + layer * 16
    base_z = i % 16
    lines_x_1_white.append((base_x, base_x+1, base_x+2, base_x+3))
    lines_y_1_white.append((base_y, base_y+4, base_y+8, base_y+12))
    lines_z_1_white.append((base_z, base_z+16, base_z+32, base_z+48))
    # length = root 2 lines
    base = layer * 16
    if i % 5 == layer:
        lines_z_ullr_white.append((base, base + 5, base + 10, base + 15))
    if i % 4 + (i // 4) % 4 == 3:
        lines_z_urll_white.append((base + 3, base + 6, base + 9, base + 12))

    if (i - 16 * layer) // 4 == layer:
        lines_x_bafo_white.append((i % 4, i % 4 + 20, i % 4 + 40, i % 4 + 60))
    if i % 12 == i % 4:
        lines_x_foba_white.append((i % 4 + 12, i % 4 + 12 + 12, i % 4 + 12 + 24, i % 4 + 12 + 36))

    if i % 4 == layer:
        lines_y_leri_white.append((i % 17, i % 17 + 17, i % 17 + 34, i % 17 + 51))
    if i % 4 + layer == 3:
        lines_y_rile_white.append((i % 15, i % 15 + 15, i % 15 + 30, i % 15 + 45))
    # length = root 3 lines
    if i % 4 == layer and (i - 16 * layer) // 4 == layer:
        upper_left_white.append((i % 21, i % 21 + 21, i % 21 + 42, i % 21 + 63))
    if i % 4 + layer == 3 and (i - 16 * layer) // 4 == layer:
        upper_right_white.append((i % 19, i % 19 + 19, i % 19 + 38, i % 19 + 57))
    if i % 4 == layer and (i - 16 * layer) // 4 + layer == 3:
        lower_left_white.append((i % 13, i % 13 + 13, i % 13 + 26, i % 13 + 39))
    if i % 4 + layer == 3 and (i - 16 * layer) // 4 + layer == 3:
        lower_right_white.append((i - 11 * layer, i - 11 * layer + 11, i - 11 * layer + 22, i - 11 * layer + 33))


def black_winning(lines_x_1_black, lines_y_1_black, lines_z_1_black, lines_z_ullr_black, lines_z_urll_black,\
                  lines_x_bafo_black, lines_x_foba_black, lines_y_leri_black, lines_y_rile_black, upper_left_black,\
                  upper_right_black, lower_left_black, lower_right_black):
    set_lines_x_1_black = set(lines_x_1_black)
    set_lines_y_1_black = set(lines_y_1_black)
    set_lines_z_1_black = set(lines_z_1_black)
    set_lines_z_ullr_black = set(lines_z_ullr_black)
    set_lines_z_urll_black = set(lines_z_urll_black)
    set_lines_x_bafo_black = set(lines_x_bafo_black)
    set_lines_x_foba_black = set(lines_x_foba_black)
    set_lines_y_leri_black = set(lines_y_leri_black)
    set_lines_y_rile_black = set(lines_y_rile_black)
    set_upper_left_black = set(upper_left_black)
    set_upper_right_black = set(upper_right_black)
    set_lower_left_black = set(lower_left_black)
    set_lower_right_black = set(lower_right_black)
    flag = ""

    for item in set_lines_x_1_black:
        count = lines_x_1_black.count(item)
        if count >= 4:
            flag = "up"
            global winning_line
            winning_line = item
    for item in set_lines_y_1_black:
        count = lines_y_1_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_z_1_black:
        count = lines_z_1_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_z_ullr_black:
        count = lines_z_ullr_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_z_urll_black:
        count = lines_z_urll_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_x_bafo_black:
        count = lines_x_bafo_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_x_foba_black:
        count = lines_x_foba_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_y_leri_black:
        count = lines_y_leri_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_y_rile_black:
        count = lines_y_rile_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_upper_left_black:
        count = upper_left_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_upper_right_black:
        count = upper_right_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lower_left_black:
        count = lower_left_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lower_right_black:
        count = lower_right_black.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    if flag == "up":
        return True
    elif flag != "up":
        return False



def white_winning(lines_x_1_white, lines_y_1_white, lines_z_1_white, lines_z_ullr_white, lines_z_urll_white,\
                  lines_x_bafo_white, lines_x_foba_white, lines_y_leri_white, lines_y_rile_white, upper_left_white,\
                  upper_right_white, lower_left_white, lower_right_white):
    set_lines_x_1_white = set(lines_x_1_white)
    set_lines_y_1_white = set(lines_y_1_white)
    set_lines_z_1_white = set(lines_z_1_white)
    set_lines_z_ullr_white = set(lines_z_ullr_white)
    set_lines_z_urll_white = set(lines_z_urll_white)
    set_lines_x_bafo_white = set(lines_x_bafo_white)
    set_lines_x_foba_white = set(lines_x_foba_white)
    set_lines_y_leri_white = set(lines_y_leri_white)
    set_lines_y_rile_white = set(lines_y_rile_white)
    set_upper_left_white = set(upper_left_white)
    set_upper_right_white = set(upper_right_white)
    set_lower_left_white = set(lower_left_white)
    set_lower_right_white = set(lower_right_white)
    flag = ""

    for item in set_lines_x_1_white:
        count = lines_x_1_white.count(item)
        if count >= 4:
            flag = "up"
            global winning_line
            winning_line = item
    for item in set_lines_y_1_white:
        count = lines_y_1_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_z_1_white:
        count = lines_z_1_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_z_ullr_white:
        count = lines_z_ullr_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_z_urll_white:
        count = lines_z_urll_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_x_bafo_white:
        count = lines_x_bafo_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_x_foba_white:
        count = lines_x_foba_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_y_leri_white:
        count = lines_y_leri_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lines_y_rile_white:
        count = lines_y_rile_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_upper_left_white:
        count = upper_left_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_upper_right_white:
        count = upper_right_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lower_left_white:
        count = lower_left_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    for item in set_lower_right_white:
        count = lower_right_white.count(item)
        if count >= 4:
            flag = "up"
            winning_line = item
    if flag == "up":
        return True
    elif flag != "up":
        return False


# showing checking


def x1(i):
    if (i // 4 * 4) % 16 == 0:
        return True


def x2(i):
    if (i // 4 * 4) % 16 == 4:
        return True


def x3(i):
    if (i // 4 * 4) % 16 == 8:
        return True


def x4(i):
    if (i // 4 * 4) % 16 == 12:
        return True


def y1(i):
    if i % 4 == 0:
        return True


def y2(i):
    if i % 4 == 1:
        return True


def y3(i):
    if i % 4 == 2:
        return True


def y4(i):
    if i % 4 == 3:
        return True


def z1(i):
    if i // 16 == 0:
        return True


def z2(i):
    if i // 16 == 1:
        return True


def z3(i):
    if i // 16 == 2:
        return True


def z4(i):
    if i // 16 == 3:
        return True


# main process
running = True
mouse = ""

while running:
    mouse_pos = pygame.mouse.get_pos()
    wn.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = "down"
            print("wow")
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse = ""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show = "all"
            if event.key == pygame.K_x:
                show = "x"
                show_number = 1
            if event.key == pygame.K_y:
                show = "y"
                show_number = 1
            if event.key == pygame.K_z:
                show = "z"
                show_number = 1
            if event.key == pygame.K_RIGHT:
                show_number += 1
                if show_number >= 4:
                    show_number = 4
                if show_number <= 1:
                    show_number = 1
            if event.key == pygame.K_LEFT:
                show_number -= 1
                if show_number >= 4:
                    show_number = 4
                if show_number <= 1:
                    show_number = 1

    # showing
    if show == "all":
        for i in range(len(block_coordinate)):
            if block_state[i] == "blue":
                wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
            if block_state[i] == "black":
                wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
            if block_state[i] == "white":
                wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
    if show == "x":
        if show_number == 1:
            for i in range(len(block_coordinate)):
                if x1(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 2:
            for i in range(len(block_coordinate)):
                if x2(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 3:
            for i in range(len(block_coordinate)):
                if x3(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 4:
            for i in range(len(block_coordinate)):
                if x4(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
    if show == "y":
        if show_number == 1:
            for i in range(len(block_coordinate)):
                if y1(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 2:
            for i in range(len(block_coordinate)):
                if y2(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 3:
            for i in range(len(block_coordinate)):
                if y3(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 4:
            for i in range(len(block_coordinate)):
                if y4(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
    if show == "z":
        if show_number == 1:
            for i in range(len(block_coordinate)):
                if z1(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 2:
            for i in range(len(block_coordinate)):
                if z2(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 3:
            for i in range(len(block_coordinate)):
                if z3(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
        if show_number == 4:
            for i in range(len(block_coordinate)):
                if z4(i):
                    if block_state[i] == "blue":
                        wn.blit(blue_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "black":
                        wn.blit(black_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))
                    if block_state[i] == "white":
                        wn.blit(white_piece, (block_coordinate[i][0] - 16, block_coordinate[i][1] - 15))



    # block
    for i in range(len(block_coordinate)):
        distance = math.sqrt(math.pow(mouse_pos[0] - block_coordinate[i][0], 2) + math.pow(mouse_pos[1] - block_coordinate[i][1], 2))
        if mouse == "down" and distance <= 15 and lock[i] != True:
            if color == "black":
                block_state[i] = "black"
                color = "white"
                lock[i] = True
                line_black(i)
            elif color == "white":
                block_state[i] = "white"
                color = "black"
                lock[i] = True
                line_white(i)

    if color == "black":
        wn.blit(black_piece, (color_coordinate[0] - 16, color_coordinate[1] - 15))
    if color == "white":
        wn.blit(white_piece, (color_coordinate[0] - 16, color_coordinate[1] - 15))

    # winning checking
    if black_winning(lines_x_1_black, lines_y_1_black, lines_z_1_black, lines_z_ullr_black, lines_z_urll_black, \
                     lines_x_bafo_black, lines_x_foba_black, lines_y_leri_black, lines_y_rile_black, upper_left_black,\
                     upper_right_black, lower_left_black, lower_right_black):
        print("game over, black wins")
        print(winning_line)
        for a in range(len(lock)):
            lock[a] = True
        for win_piece in winning_line:
            wn.blit(red_piece, (block_coordinate[win_piece][0]-16, block_coordinate[win_piece][1]-15))
        color = "black"
    if white_winning(lines_x_1_white, lines_y_1_white, lines_z_1_white, lines_z_ullr_white, lines_z_urll_white, \
                     lines_x_bafo_white, lines_x_foba_white, lines_y_leri_white, lines_y_rile_white, upper_left_white,\
                     upper_right_white, lower_left_white, lower_right_white):
        print("game over, white wins")
        print(winning_line)
        for a in range(len(lock)):
            lock[a] = True
        for win_piece in winning_line:
            wn.blit(red_piece, (block_coordinate[win_piece][0]-16, block_coordinate[win_piece][1]-15))
            color = "white"

    pygame.display.update()
