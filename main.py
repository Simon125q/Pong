import sys

import pygame


def check_event():
    """
    check what key is pressed
    """
    global player1, player2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player2.top > win.top:
                    player2 = player2.move(0, -step)
            if event.key == pygame.K_DOWN:
                if player2.bottom < win.bottom:
                    player2 = player2.move(0, step)
            if event.key == event.key == ord('w'):
                if player1.top > win.top:
                    player1 = player1.move(0, -step)
            if event.key == event.key == ord('s'):
                if player1.bottom < win.bottom:
                    player1 = player1.move(0, step)


def check_collision():
    """
    checks collisions of the ball
    and change vector accordingly
    """
    global ball, score2, score1, vec
    # ball against the walls
    if ball.left < win.left or ball.right > win.right:
        if ball.left < win.left:
            score2 += 1
            ball.center = (width - int(width / 3), int(height / 2))
        if ball.right > win.right:
            score1 += 1
            ball.center = (int(width / 3), int(height / 2))
        vec[1] = -vec[1]
        pygame.time.wait(700)
    if ball.top < win.top or ball.bottom > win.bottom:
        if ball.top < win.top:
            ball = ball.move((0, 1))
        if ball.bottom > win.bottom:
            ball = ball.move((0, -1))
        vec[1] = -vec[1]
    # ball against player 1
    if ball.left < player1.right and abs(ball.centery - player1.centery) < (ball.h + player1.h) / 2:
        ball = ball.move((3, 0))
        vec[0] = -vec[0]
    if ball.bottom > player1.top > ball.top and ball.left < player1.right:
        ball = ball.move((0, -5))
        vec[1] = -vec[1]
    if ball.top < player1.bottom < ball.bottom and ball.left < player1.right:
        ball = ball.move((0, 5))
        vec[1] = -vec[1]
    # ball against player 2
    if ball.right > player2.left and abs(ball.centery - player2.centery) < (ball.h + player2.h) / 2:
        ball = ball.move((-3, 0))
        vec[0] = -vec[0]
    if ball.bottom > player2.top > ball.top and ball.right > player2.left:
        ball = ball.move((0, -5))
        vec[1] = -vec[1]
    if ball.top < player2.bottom < ball.bottom and ball.right > player2.left:
        ball = ball.move((0, 5))
        vec[1] = -vec[1]


def check_win():
    """
    checks if any player has 10 points
    if yes displays winning window
    and end the game
    """
    if score1 == 10 or score2 == 10:
        if score1 == 10:
            scr.blit(msg_win_1, msg_box_win_1)
        if score2 == 10:
            scr.blit(msg_win_2, msg_box_win_2)
        pygame.display.flip()
        pygame.time.wait(5000)
        sys.exit()


def increase_difficulty():
    """
    increases difficulty after
    one of players scores 3 points
    and after scores 6 points
    """
    if score1 == 3 or score2 == 3:
        if vec[0] < 0:
            vec[0] = -3
        else:
            vec[0] = 3
        if vec[1] < 0:
            vec[1] = -2
        else:
            vec[1] = 2
    if score1 >= 6 or score2 >= 6:
        if vec[1] < 0:
            vec[1] = -3
        else:
            vec[1] = 3


def display():
    """
    updates what is displayed
    """
    global msg
    scr.fill(black)
    msg = myfont.render(f"SCORE {score1} : {score2}", True, yellow)
    for i in range(int(height / line[2])):
        pygame.draw.rect(scr, white, line)
        line.midtop = (width / 2, 50 * i)
    scr.blit(msg, msg_box)
    pygame.draw.rect(scr, white, ball)
    pygame.draw.rect(scr, white, player1)
    pygame.draw.rect(scr, white, player2)
    pygame.display.flip()


if __name__ == "__main__":
    # variables
    score1, score2 = 0, 0
    step = 20
    vec = [2, 1]
    black = (0, 0, 0)
    yellow = (255, 204, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    width = 1300
    height = 800

    pygame.init()
    # objects
    scr = pygame.display.set_mode((width, height))
    win = scr.get_rect()
    line = pygame.Rect(0, 0, 15, 25)
    line.midtop = win.midtop
    ball = pygame.Rect(0, 0, 30, 30)
    ball.center = (int(width / 3), int(height / 2))
    player1 = pygame.Rect(0, 0, 30, height / 6)
    player1.midleft = win.midleft
    player2 = pygame.Rect(0, 0, 30, height / 6)
    player2.midright = win.midright
    # messages
    myfont = pygame.font.Font('freesansbold.ttf', 48)
    myfont_big = pygame.font.Font('freesansbold.ttf', 90)
    msg = myfont.render(f"SCORE {score1} : {score2}", True, yellow)
    msg_win_1 = myfont_big.render("Player 1 Wins!", True, red)
    msg_win_2 = myfont_big.render("Player 2 Wins!", True, red)
    msg_box_win_1 = msg_win_1.get_rect()
    msg_box_win_1.center = win.center
    msg_box_win_2 = msg_win_2.get_rect()
    msg_box_win_2.center = win.center
    msg_box = msg.get_rect()
    msg_box.midtop = win.midtop
    msg_start = myfont_big.render("Welcome to PONG game!", True, red)
    msg_box_start = msg_start.get_rect()
    msg_box_start.midtop = win.midtop
    msg_start2 = myfont.render("Player who first scores 10 points wins", True, yellow)
    msg_box_start2 = msg_start2.get_rect()
    msg_box_start2.midtop = win.center

    pygame.key.set_repeat(50, 50)
    fps = pygame.time.Clock()
    # starting window
    scr.blit(msg_start, msg_box_start)
    scr.blit(msg_start2, msg_box_start2)
    pygame.display.flip()
    pygame.time.wait(5000)
    # forever loop
    while True:
        # main logic

        check_event()

        check_collision()

        ball = ball.move(vec)

        check_win()

        increase_difficulty()

        display()

        fps.tick(240)
