import pygame
import random
pygame.init()

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (124, 252, 0)
BLUE = (0, 191, 255)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)
pale_white = (220, 223, 227)
hover_color = (255, 255, 255)
hover_color_exit = (255, 255, 255)
hover_color_play = (255, 255, 255)

#Positions
positions = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

#Sounds
pygame.mixer.music.load('boogie.mp3')
pygame.mixer.music.play(-1)
x_sound = pygame.mixer.Sound("cowbell.wav")
o_sound = pygame.mixer.Sound("boing.wav")
click = pygame.mixer.Sound("click.wav")
cheer = pygame.mixer.Sound("cheer.wav")
boo = pygame.mixer.Sound("boo.wav")
sound = 0


# Misc
number = random.randint(1, 2)
dict = {1: "X", 2: "O", 3: "No one"}
winner = None
score_x = 0
score_o = 0
pause = 0

# Screen
src_width = 600
src_height = 700
screen = pygame.display.set_mode((src_width, src_height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)
title = pygame.font.Font('freesansbold.ttf', 90)
play = pygame.font.Font('freesansbold.ttf', 50)
scoreboardfont = pygame.font.Font('freesansbold.ttf', 20)
end = 1.0
start = False
first = False

def ending (positions):
    win = 3
    if positions[0][0] == positions[0][1] == positions[0][2] and positions[0][0] != 0:
        win = positions[0][0]

    if positions[1][0] == positions[1][1] == positions[1][2] and positions[1][0] != 0:
        win = positions[1][0]

    if positions[2][0] == positions[2][1] == positions[2][2] and positions[2][0] != 0:
        win = positions[2][0]

    if positions[0][0] == positions[1][0] == positions[2][0] and positions[0][0] != 0:
        win = positions[0][0]

    if positions[0][1] == positions[1][1] == positions[2][1] and positions[0][1] != 0:
        win = positions[0][1]

    if positions[0][2] == positions[1][2] == positions[2][2] and positions[0][2] != 0:
        win = positions[0][2]

    if positions[0][0] == positions[1][1] == positions[2][2] and positions[0][0] != 0:
        win = positions[0][0]

    if positions[0][2] == positions[1][1] == positions[2][0] and positions[1][1] != 0:
        win = positions[0][2]


    return win

replay = True

run = True
while replay == True:
    screen.fill(BLACK)
    run = True
    winner = None
    sound = 0
    pause = 0
    while run == True:

        caption = title.render('Tic Tac Toe', True, WHITE)
        captionRect = caption.get_rect()
        captionRect.center = (300, 200)
        title_bg = title.render('Tic Tac Toe', True, pale_white)
        titleRect = title_bg.get_rect()
        titleRect.center = (304, 204)

        text = play.render('Play', True, hover_color)
        textRect = text.get_rect()
        textRect.center = (300, 650)
        exit = play.render('Exit', True, hover_color_exit)
        exitRect = exit.get_rect()
        exitRect.center = (300, 350)
        scoreboardO = scoreboardfont.render('Os score:' + str(score_o), True, WHITE)
        scoreboardX = scoreboardfont.render('Xs score:' + str(score_x), True, WHITE)
        scoreboardORect = scoreboardO.get_rect()
        scoreboardXRect = scoreboardX.get_rect()
        scoreboardORect.center = (80, 650)
        scoreboardXRect.center = (500, 650)
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if not start:
            screen.blit(title_bg, titleRect)
            screen.blit(caption, captionRect)
            screen.blit(text, textRect)
            screen.blit(exit, exitRect)
            pygame.display.update()


            if 256 <= pos[0] <= 341 and 328 <= pos[1] <= 362:
                hover_color_exit = RED
                if pressed1 == 1:
                    run = False
                    replay = False

            if 341 < pos[0] or pos[0] < 256 or 362 < pos[1] or pos[1] < 330:
                hover_color_exit = WHITE

            if 253 <= pos[0] <= 351 and 628 <= pos[1] <= 663:
                hover_color = GREEN
                if pressed1 == 1:
                    start = True
                    pygame.mixer.Sound.play(click)
                    end = 2.0
                    hit = 0

            if 351 < pos[0] or pos[0] < 253 or 663 < pos[1] or pos[1] < 628:
                hover_color = WHITE

        if start == True:
            screen.blit(scoreboardX, scoreboardXRect)
            screen.blit(scoreboardO, scoreboardORect)
            pygame.display.update()
            if first == False:
                pygame.display.update(pygame.draw.rect(screen, BLACK, (0, 0, 600, 600)))
                first = True

            pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 0, 5, 600)))
            pygame.display.update(pygame.draw.rect(screen, GREEN, (200, 0, 5, 600)))
            pygame.display.update(pygame.draw.rect(screen, GREEN, (400, 0, 5, 600)))
            pygame.display.update(pygame.draw.rect(screen, GREEN, (595, 0, 5, 600)))
            pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 0, 600, 5)))
            pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 200, 600, 5)))
            pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 400, 600, 5)))
            pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 595, 600, 5)))


            if dict[number] == "O":
                pygame.display.update(pygame.draw.rect(screen, BLACK, (150, 620, 300, 70)))
                pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 650), 30, 3))

            if dict[number] == "X":
                pygame.display.update(pygame.draw.rect(screen, BLACK, (150, 620, 300, 70)))
                pygame.display.update(pygame.draw.line(screen, ORANGE, (280, 632), (320, 669), 5))
                pygame.display.update(pygame.draw.line(screen, ORANGE, (320, 632), (280, 669), 5))

            if pressed1 == True and end/4 == 0.75:
                if 0 < pos[0] < 200 and 0 < pos[1] < 200:

                    if dict[number] == "X" and positions[0][0] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (0, 0), (200, 200), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 0), (0, 200), 10))
                        number += 1
                        positions[0][0] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[0][0] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (100, 100), 90, 10))
                        number -= 1
                        positions[0][0] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 200 < pos[0] < 400 and 0 < pos[1] < 200:

                    if dict[number] == "X" and positions[0][1] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 0), (400, 200), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 0), (200, 200), 10))
                        number += 1
                        positions[0][1] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[0][1] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 100), 90, 10))
                        number -= 1
                        positions[0][1] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 400 < pos[0] < 600 and 0 < pos[1] < 200:
                    if dict[number] == "X" and positions[0][2] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 0), (600, 200), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (600, 0), (400, 200), 10))
                        number += 1
                        positions[0][2] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[0][2] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (500, 100), 90, 10))
                        number -= 1
                        positions[0][2] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 0 < pos[0] < 200 and 200 < pos[1] < 400:

                    if dict[number] == "X" and positions[1][0] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (0, 200), (200, 400), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 200), (0, 400), 10))
                        number += 1
                        positions[1][0] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[1][0] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (100, 300), 90, 10))
                        number -= 1
                        positions[1][0] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 200 < pos[0] < 400 and 200 < pos[1] < 400:

                    if dict[number] == "X" and positions[1][1] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 200), (400, 400), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 200), (200, 400), 10))
                        number += 1
                        positions[1][1] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[1][1] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 300), 90, 10))
                        number -= 1
                        positions[1][1] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 400 < pos[0] < 600 and 200 < pos[1] < 400:
                    if dict[number] == "X" and positions[1][2] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 200), (600, 400), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (600, 200), (400, 400), 10))
                        number += 1
                        positions[1][2] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[1][2] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (500, 300), 90, 10))
                        number -= 1
                        positions[1][2] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 0 < pos[0] < 200 and 400 < pos[1] < 600:

                    if dict[number] == "X" and positions[2][0] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (0, 400), (200, 600), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 400), (0, 600), 10))
                        number += 1
                        positions[2][0] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[2][0] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (100, 500), 90, 10))
                        number -= 1
                        positions[2][0] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 200 < pos[0] < 400 and 400 < pos[1] < 600:

                    if dict[number] == "X" and positions[2][1] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 400), (400, 600), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 400), (200, 600), 10))
                        number += 1
                        positions[2][1] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[2][1] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 500), 90, 10))
                        number -= 1
                        positions[2][1] = 2
                        pygame.mixer.Sound.play(o_sound)

                if 400 < pos[0] < 600 and 400 < pos[1] < 600:
                    if dict[number] == "X" and positions[2][2] == 0:
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 400), (600, 600), 10))
                        pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 600), (600, 400), 10))
                        number += 1
                        positions[2][2] = 1
                        pygame.mixer.Sound.play(x_sound)

                    if dict[number] == "O" and positions[2][2] == 0:
                        pygame.display.update(pygame.draw.circle(screen, BLUE, (500, 500), 90, 10))
                        number -= 1
                        positions[2][2] = 2
                        pygame.mixer.Sound.play(o_sound)

            if end != True:
                end = 3.0

            if positions[0][0] == positions[0][1] == positions[0][2] and positions[0][0] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (10, 100), (590, 100), 10))
                end = True


            if positions[1][0] == positions[1][1] == positions[1][2] and positions[1][0] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (10, 300), (590, 300), 10))
                end = True


            if positions[2][0] == positions[2][1] == positions[2][2] and positions[2][0] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (10, 500), (590, 500), 10))
                end = True


            if positions[0][0] == positions[1][0] == positions[2][0] and positions[0][0] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (100, 10), (100, 590), 10))
                end = True


            if positions[0][1] == positions[1][1] == positions[2][1] and positions[0][1] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (300, 10), (300, 590), 10))
                end = True


            if positions[0][2] == positions[1][2] == positions[2][2] and positions[0][2] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (500, 10), (500, 590), 10))
                end = True


            if positions[0][0] == positions[1][1] == positions[2][2] and positions[0][0] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (10, 10), (590, 590), 10))
                end = True


            if positions[0][2] == positions[1][1] == positions[2][0] and positions[1][1] != 0:
                pygame.display.update(pygame.draw.line(screen, GREEN, (590, 10), (10, 590), 10))
                end = True

            index = 0
            for i in range(0, 3):
                for j in range(0, 3):

                    if positions[i][j] != 0:
                        index += 1

            if index == 9:
                end = True

            if end == True:
                if pause == 10:
                    screen.fill(BLACK)
                    pygame.mixer.music.stop()

                    winner = ending(positions)
                    if dict[winner] == "O":
                        title_bg = title.render(dict[winner] + " Wins", True, BLUE)

                        if sound == 0:
                            pygame.mixer.Sound.play(cheer)
                            score_o += 1
                            sound += 1

                    elif dict[winner] == "X":
                        title_bg = title.render(dict[winner] + " Wins", True, ORANGE)

                        if sound == 0:
                            pygame.mixer.Sound.play(cheer)
                            score_x += 1
                            sound += 1
                    else:
                        title_bg = title.render(dict[winner] + " Wins", True, WHITE)
                        if sound == 0:
                            pygame.mixer.Sound.play(boo)
                            sound += 1
                    titleRect = title_bg.get_rect()
                    titleRect.center = (300, 200)
                    exit = play.render('Exit', True, hover_color_exit)
                    exitRect = exit.get_rect()
                    exitRect.center = (300, 350)
                    playAgain = play.render('Play', True, hover_color_play)
                    playRect = playAgain.get_rect()
                    playRect.center = (300, 650)

                    if 249 <= pos[0] <= 345 and 629 <= pos[1] <= 662:
                        hover_color_play = GREEN
                        if pressed1 == 1:
                            positions = [[0, 0, 0],
                                         [0, 0, 0],
                                         [0, 0, 0]]
                            pygame.mixer.stop()
                            pygame.mixer.music.load('boogie.mp3')
                            pygame.mixer.music.play(-1)

                            end = False
                            run = False

                    else:
                        hover_color_play = WHITE

                    if 254 <= pos[0]<= 343 and 329 <= pos[1] <= 361:
                        hover_color_exit = RED
                        if pressed1 == 1:
                            run = False
                            replay = False

                    else:
                        hover_color_exit = WHITE




                    screen.blit(title_bg, titleRect)
                    screen.blit(playAgain, playRect)
                    screen.blit(exit, exitRect)
                    screen.blit(scoreboardX, scoreboardXRect)
                    screen.blit(scoreboardO, scoreboardORect)
                    pygame.display.update()
                else:
                    pause += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                replay = False


pygame.quit()
quit()

