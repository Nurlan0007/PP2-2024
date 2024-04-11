import pygame, random, math
pygame.init()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW = (192, 192, 192)
ORANGE = (255,100,10)
GREY = (127,127,127)
NAVY_BLUE = (0,0,100)
POWDERBLUE = (176, 224, 230, 255)
YELLOW = (255, 255, 0)
PURPLE = (153, 0, 153)


def draw_line(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


def save_image(Surface, name):
    file = open('exist_check.txt', 'r')
    f = file.read()
    pygame.image.save(Surface ,('/Users/Владелец/Desktop/q/lab9/saved_images/' + name + str(int(f)) + '.png'))
    file = open('exist_check.txt', 'w')
    file.write(str(int(f) + 1))
    file.close()

def main():
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('pain(t)')
    icon = pygame.image.load("./resources/icon.png")
    pygame.display.set_icon(icon)

    pygame.draw.rect(screen, SHADOW, (900, 0, 900, 700))
    pygame.draw.line(screen, GREY, (904, 0), (904, 700), 3)
    pygame.draw.line(screen, GREY, (1, 0), (1, 700), 3)
    pygame.draw.line(screen, GREY, (0, 698), (1000, 698), 3)
    pygame.draw.line(screen, GREY, (0, 1), (1000, 1), 3)
    pygame.draw.line(screen, GREY, (998, 0), (998, 700), 3)

    font = pygame.font.SysFont("Verdana", 20)
    tools_txt = font.render('Tools:', True, BLACK)

    screen.blit(tools_txt, (910, 119))
    pygame.draw.rect(screen, GREY, (910, 145, 80, 120), 2)
    pygame.draw.line(screen, GREY, (950, 145), (950, 225), 2)
    pygame.draw.line(screen, GREY, (910, 185), (990, 185), 2)
    pygame.draw.line(screen, GREY, (910, 225), (990, 225), 2)
    pygame.draw.line(screen, GREY, (0, 697), (900, 697), 2)

    brush_png = pygame.transform.scale(pygame.image.load("./resources/brush.png"), (20,20))
    eraser_png = pygame.transform.scale(pygame.image.load("./resources/eraser.png"), (20,20))
    clear_png = pygame.transform.scale(pygame.image.load("./resources/clear.png"), (30, 30))
    save_png = pygame.transform.scale(pygame.image.load("./resources/save.png"), (98, 50))

    pygame.draw.rect(screen, BLACK, (918, 197, 25, 15), 2)
    pygame.draw.circle(screen, BLACK, (970, 205), 9, 2)

    global brush, eraser, clear, save
    save = screen.blit(save_png, (902, 40))
    screen.blit(clear_png, (936, 230)) 
    screen.blit(brush_png, (920, 156))
    screen.blit(eraser_png, (960, 158))
    colors_txt = font.render('Colors:', True, BLACK)
    screen.blit(colors_txt, (910, 450))
    pygame.draw.rect(screen, GREY, (925, 485, 50, 175), 2)
    clr_list = [RED, ORANGE, YELLOW, GREEN, POWDERBLUE, BLUE, PURPLE, BLACK]
    clr_rect_list = []
    for cl, i in enumerate(range(485, 685, 25), 0):
        pygame.draw.rect(screen, clr_list[cl], (925, i, 50, 25))
        clr_rect_list.append(pygame.Rect((925, i, 50, 25)))

    

    def size_buttons():
        global button
        sz_txt = font.render('Size - ', True, BLACK)
        screen.blit(sz_txt, (909, 298)) 
        pygame.draw.rect(screen, GREY, (910, 335, 80, 80), 2)
        screen.fill(WHITE, (912, 337, 77, 77))
        sz_btn = pygame.transform.scale(pygame.image.load("./resources/updown.png"), (25, 25))
        button = screen.blit(sz_btn, (970, 300))
        pygame.display.flip()


    rect_button = pygame