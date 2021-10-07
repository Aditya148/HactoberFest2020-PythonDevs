import pygame
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'  # THIS LINE IS USED TO CENTER THE WINDOW

pygame.init()  # INITIALIZING pygame
pygame.mixer.init()  # INITIALIZING pygame.mixer
font = pygame.font.Font('files/fonts/revue.ttf', 50)  # LOADING THE FONT FILE FROM THE PATH AND SIZE OF IT IS 50.
game_font = pygame.font.Font('files/fonts/revue.ttf', 30)  # LOADING THE FONT FILE FROM THE PATH AND SIZE OF IT IS 30.
pygame.mixer.music.load('files/sounds/music.mp3')
pygame.mixer.music.play(-1, 3.0)  # -1 IS USED FOR LOOP AND 3.0 MEANS THAT MUSIC WILL START FROM 3.0 SECONDS
clock = pygame.time.Clock()  # ADDING CLOCK FOR SETTING THE FPS

# COLORS #
WHITE = (225, 225, 225)  # PUTTING HEX WHITE COLOR IN A VARIABLE (WHITE)
BLACK = (60, 60, 60)  # PUTTING HEX GREY COLOR IN A VARIABLE (BLACK)

screen = pygame.display.set_mode((1000, 600))  # SETTING THE WINDOW SIZE OF THE GAME
pygame.display.set_caption("TABLE TENNIS GAME (DEV - UTPAL)")  # SETTING THE TITLE OF THE GAME WINDOW
programIcon = pygame.image.load('files/textures/pong.ico')
pygame.display.set_icon(programIcon)

# VARIABLES #
FPS = 60  # FPS = FRAME PER SECOND
running = True
click = False
clicked = False
clicking = False
player = pygame.Rect(10, 230, 30, 140)
opponent = pygame.Rect(960, 230, 30, 140)
ball = pygame.Rect(481, 281, 38, 38)
player_change, ballX, ballY, opponent_change = 0, 7, 7, 0
player_score, opponent_score = 0, 0
score_time = 0


# ================================= GAME AREA FUNCTION ========================================== #
def start():
    global ballX, ballY, score_time, game_font

    current_time = pygame.time.get_ticks()
    ball.center = (500, 300)
    one, two, three = "1", "2", "3"

    if current_time - score_time < 700:
        number_three = game_font.render(str(three), True, BLACK)
        screen.blit(number_three, (492, 288))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render(str(two), True, BLACK)
        screen.blit(number_two, (492, 288))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render(str(one), True, BLACK)
        screen.blit(number_one, (492, 288))

    if current_time - score_time < 2100:
        ballX, ballY = 0, 0
    else:
        ballX = random.choice((7, -7))
        ballY = random.choice((7, -7))
        score_time = 0


def game():
    global running, player_score, opponent_score, score_time, player_change, opponent_change, ballX, ballY
    pop = pygame.mixer.Sound('files/sounds/pop.wav')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if player.y <= 10:
                        player_change = 0
                    else:
                        player_change = -7
                if event.key == pygame.K_s:
                    if player.y >= 600 - 150:
                        player_change = 0
                    else:
                        player_change = 7
                if event.key == pygame.K_UP:
                    if opponent.y <= 10:
                        opponent_change = 0
                    else:
                        opponent_change = -7
                if event.key == pygame.K_DOWN:
                    if opponent.y >= 600 - 150:
                        opponent_change = 0
                    else:
                        opponent_change = 7

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.rect(screen, WHITE, opponent)
        pygame.draw.aaline(screen, WHITE, (500, 0), (500, 600))

        player_text = game_font.render(f"{player_score}", True, WHITE)
        screen.blit(player_text, (500 - 50, 300 - 15))

        opponent_text = game_font.render(f"{opponent_score}", True, WHITE)
        screen.blit(opponent_text, (500 + 35, 300 - 15))

        if score_time:
            start()

        pygame.display.update()
        clock.tick(FPS)

        # PLAYER MOVEMENT #
        player.y += player_change
        if player.y <= 10:
            player_change = 0
        if player.y >= 600 - 150:
            player_change = 0

        # OPPONENT MOVEMENT #
        opponent.y += opponent_change
        if opponent.y <= 10:
            opponent_change = 0
        if opponent.y >= 600 - 150:
            opponent_change = 0

        # BALL MOVEMENT #
        ball.x += ballX
        ball.y += ballY

        if ball.y >= 600 - 38:
            ballY = -7
        if ball.y <= 0:
            ballY = 7
        if ball.x >= 1000 - 38:
            start()
            player_score += 1
            score_time = pygame.time.get_ticks()
        if ball.x <= 0:
            start()
            opponent_score += 1
            score_time = pygame.time.get_ticks()
        if ball.colliderect(player):
            pop.play()
            ballX = 7
        if ball.colliderect(opponent):
            pop.play()
            ballX = -7


# =============================== START MENU FUNCTION ================================= #
def menu():
    def __quit__():
        quit()

    global running, clicked
    main_font = pygame.font.Font('files/fonts/capsconst.ttf', 50)  # LOADING FONT AND SIZE OF IT IS 50.
    screen.fill(BLACK)  # FILLING THE GREY(LIGHT BLACK) COLOR ON THE SCREEN TO HIDE PREVIOUS OBJECTS

    heading = main_font.render("MAIN MENU", True, WHITE)  # (1)TEXT, (2)ANTI-ALIASING, (3)COLOR OF FONT
    screen.blit(heading, (30, 30))  # DISPLAYING THE ABOVE TEXT

    pic = pygame.image.load('files/textures/pong.png')  # LOADING AN IMAGE
    screen.blit(pic, (100, 150))  # DISPLAYING ABOVE IMAGE

    play_game_rect = pygame.Rect(545, 195, 380, 60)  # MAKING A RECTANGLE OF DESIRED SIDES
    play_game = main_font.render("PLAY GAME", True, WHITE)  # (1)TEXT, (2)ANTI-ALIASING, (3)COLOR OF FONT
    screen.blit(play_game, (550, 200))  # DISPLAYING THE ABOVE TEXT
    pygame.draw.rect(screen, BLACK, play_game_rect, 1)  # DISPLAYING THE ABOVE RECTANGLE

    exit_game_rect = pygame.Rect(545, 295, 405, 60)  # MAKING A RECTANGLE OF DESIRED SIDES
    exit_game = main_font.render("EXIT GAME", True, WHITE)  # (1)TEXT, (2)ANTI-ALIASING, (3)COLOR OF FONT
    screen.blit(exit_game, (550, 300))  # DISPLAYING THE ABOVE TEXT
    pygame.draw.rect(screen, BLACK, exit_game_rect, 1)  # DISPLAYING THE ABOVE RECTANGLE

    pygame.display.update()  # UPDATING THE SCREEN (TO MAKE OBJECTS VISIBLE)

    while running:  # MAKING A INFINITE WHILE LOOP THAT WILL STOP WHEN USER QUITS THE GAME
        for events in pygame.event.get():
            if events.type == pygame.QUIT:  # WHEN USER CLICKS ON CLOSE BUTTON THEN THE LOOP WILL END AND GAME ENDS
                running = False
            if events.type == pygame.MOUSEBUTTONUP:
                if events.button == 1:
                    x, y = pygame.mouse.get_pos()  # THIS WILL GET THE RELEASE POSITION
                    clicked = True
                    if play_game_rect.collidepoint(x, y):
                        if clicked:
                            game()
                    if exit_game_rect.collidepoint(x, y):
                        if clicked:
                            __quit__()

        pygame.display.update()
        clock.tick(FPS)


while running:  # MAKING A INFINITE WHILE LOOP THAT WILL STOP WHEN USER QUITS THE GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # WHEN USER CLICKS ON CLOSE BUTTON THEN THE LOOP WILL END AND GAME ENDS
            running = False
        if event.type == pygame.KEYUP:  # IF ANY BUTTON IS RELEASED
            if event.key == pygame.K_SPACE:  # WHEN SPACEBAR IS PRESSED THEN IT WILL CHANGE THE VALUE OF VARIABLE TO TRUE
                click = True

    screen.fill(BLACK)  # FILL THE BLACK COLOR TO THE SCREEN

    box = pygame.Rect(50, 50, 900, 500)  # MAKING A RECTANGLE OF DESIRED LENGTH
    pygame.draw.rect(screen, WHITE, box, 3)  # DRAWING THE ABOVE RECTANGLE ON THE SCREEN

    image = pygame.image.load('files/textures/pong.png')  # LOADING THE IMAGE TO THE VARIABLE
    screen.blit(image, (320, 80))  # DISPLAY THE ABOVE IMAGE AT DESIRED LOCATION

    ahead = font.render('PRESS SPACEBAR TO CONTINUE', True, WHITE)  # LOADING TEXT
    screen.blit(ahead, (85, 480))  # DISPLAYING TEXT ON THE SCREEN AT DESIRED POSITION

    if click:  # IF VALUE OF click VARIABLE IS True THEN CALL menu() FUNCTION
        menu()

    pygame.display.update()  # USED TO UPDATE THE SCREEN (FOR MAKING OBJECT ABOVE VISIBLE ON THE SCREEN)
    clock.tick(FPS)
