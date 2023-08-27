import pygame
import random
width = 300
height = 300
fps = 30
pink = 255, 0, 123
cyan = 0, 161, 161
red = 255, 0, 0
gold = 229, 223, 34
black = 0, 0, 0
pygame.init()
field = [["","",""], ["","",""], ["","",""]]
gameover = False
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крестики-нолики")
run = True
clock = pygame.time.Clock()
def grid():
    pygame.draw.line(screen, cyan, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, cyan, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, cyan, (0, 100), (300,100), 3)
    pygame.draw.line(screen, cyan, (0, 200), (300, 200), 3)
def draw():
    for a in range(3):
        for b in range(3):
            if field[a][b] == "0":
                pygame.draw.circle(screen, black, (b*100 + 50, a*100 + 50), 50, 3)
            elif field[a][b] == "x":
                pygame.draw.line(screen, black, (b*100 + 5, a*100 + 5), (b*100 + 95, a*100 + 95), 3)
                pygame.draw.line(screen, black, (b*100 + 95, a*100 + 5), (b*100 + 5, a*100 + 95), 3)
def wincheck(symbol):
    flag_win = False
    global win
    for line in field:
        if line.count(symbol) == 3:
            flag_win = True
            win = [[0, field.index(line)], [1, field.index(line)], [2, field.index(line)]]
    for a in range(3):
        if field[0][a] == field[1][a] == field[2][a] == symbol:
            flag_win = True
            win = [[a, 0], [a, 1], [a, 2]]
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
    if  field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]
    return flag_win
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not gameover:            
            pos = pygame.mouse.get_pos()
            if field[pos[1]//100][pos[0]//100] == "":
                field[pos[1]//100][pos[0]//100] = "x"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "0"
            playerwin = wincheck("x")
            computerwin = wincheck("0")
            result = field[0].count("x") + field[0].count("0") + field[1].count("x") + field[1].count("0") + field[2].count("x") + field[2].count("0")
            if playerwin or computerwin:
                gameover = True
                if computerwin:
                    pygame.display.set_caption("Компьютер победил")
                else:
                    pygame.display.set_caption("Игрок победил")
            elif result == 8:
                pygame.display.set_caption("Ничья")


    screen.fill(pink)
    if gameover:
        pygame.draw.rect(screen, gold, (win[0][0]*100, win[0][1]*100, 100, 100))
        pygame.draw.rect(screen, gold, (win[1][0]*100, win[1][1]*100, 100, 100))
        pygame.draw.rect(screen, gold, (win[2][0]*100, win[2][1]*100, 100, 100))
    grid()
    draw()
    pygame.display.flip()
pygame.quit()
