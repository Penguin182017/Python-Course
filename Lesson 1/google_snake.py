import pygame
import random

pygame.init()

# ==================================================
# SETTINGS
# ==================================================

WIDTH = 800
HEIGHT = 600

CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 60, bold=True)

# ==================================================
# COLORS
# ==================================================

LIGHT_GREEN = (170, 215, 81)
DARK_GREEN = (162, 209, 73)

SNAKE_GREEN = (76, 175, 80)
SNAKE_DARK = (56, 142, 60)

APPLE_RED = (220, 50, 50)

WHITE = (255, 255, 255)
BLACK = (40, 40, 40)

# ==================================================
# GAME VARIABLES
# ==================================================

snake = []

direction = [CELL, 0]
next_direction = [CELL, 0]

apple = [0, 0]

score = 0
high_score = 0

game_over = False
paused = False


# ==================================================
# CREATE APPLE
# ==================================================

def create_apple():

    global apple

    while True:

        apple = [
            random.randrange(0, WIDTH, CELL),
            random.randrange(0, HEIGHT, CELL)
        ]

        if apple not in snake:
            break


# ==================================================
# RESTART
# ==================================================

def restart_game():

    global snake
    global direction
    global next_direction
    global score
    global game_over
    global paused

    # Start in the middle

    snake = [
        [400, 300],
        [380, 300],
        [360, 300],
        [340, 300]
    ]

    direction = [CELL, 0]
    next_direction = [CELL, 0]

    score = 0

    game_over = False
    paused = False

    create_apple()


# ==================================================
# DRAW BOARD
# ==================================================

def draw_board():

    for y in range(0, HEIGHT, CELL):

        for x in range(0, WIDTH, CELL):

            if (x // CELL + y // CELL) % 2 == 0:

                color = LIGHT_GREEN

            else:

                color = DARK_GREEN

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL, CELL)
            )


# ==================================================
# DRAW APPLE
# ==================================================

def draw_apple():

    center_x = apple[0] + CELL // 2
    center_y = apple[1] + CELL // 2

    # Apple

    pygame.draw.circle(
        screen,
        APPLE_RED,
        (center_x, center_y + 1),
        8
    )

    # Small leaf

    pygame.draw.ellipse(
        screen,
        SNAKE_GREEN,
        (
            center_x + 2,
            center_y - 10,
            7,
            4
        )
    )


# ==================================================
# DRAW SNAKE
# ==================================================

def draw_snake():

    for i, part in enumerate(snake):

        x = part[0]
        y = part[1]

        # Small gap between segments

        rect = pygame.Rect(
            x + 1,
            y + 1,
            CELL - 2,
            CELL - 2
        )

        if i == 0:

            # HEAD

            pygame.draw.rect(
                screen,
                SNAKE_GREEN,
                rect,
                border_radius=7
            )

            # Eyes

            if direction == [CELL, 0]:

                eye1 = (x + 14, y + 6)
                eye2 = (x + 14, y + 14)

            elif direction == [-CELL, 0]:

                eye1 = (x + 6, y + 6)
                eye2 = (x + 6, y + 14)

            elif direction == [0, -CELL]:

                eye1 = (x + 6, y + 6)
                eye2 = (x + 14, y + 6)

            else:

                eye1 = (x + 6, y + 14)
                eye2 = (x + 14, y + 14)

            pygame.draw.circle(
                screen,
                WHITE,
                eye1,
                3
            )

            pygame.draw.circle(
                screen,
                WHITE,
                eye2,
                3
            )

            pygame.draw.circle(
                screen,
                BLACK,
                eye1,
                1
            )

            pygame.draw.circle(
                screen,
                BLACK,
                eye2,
                1
            )

        else:

            # BODY

            pygame.draw.rect(
                screen,
                SNAKE_GREEN,
                rect,
                border_radius=6
            )


# ==================================================
# START
# ==================================================

restart_game()

running = True


# ==================================================
# MAIN GAME LOOP
# ==================================================

while running:

    # ==================================================
    # EVENTS
    # ==================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            # ------------------------------------------
            # RESTART
            # ------------------------------------------

            if event.key == pygame.K_r and game_over:

                if score > high_score:
                    high_score = score

                restart_game()

            # ------------------------------------------
            # PAUSE
            # ------------------------------------------

            if event.key == pygame.K_p and not game_over:

                paused = not paused

            # ------------------------------------------
            # MOVEMENT
            # ------------------------------------------

            if not game_over and not paused:

                # UP

                if event.key in (
                    pygame.K_UP,
                    pygame.K_w
                ):

                    if direction != [0, CELL]:

                        next_direction = [0, -CELL]

                # DOWN

                elif event.key in (
                    pygame.K_DOWN,
                    pygame.K_s
                ):

                    if direction != [0, -CELL]:

                        next_direction = [0, CELL]

                # LEFT

                elif event.key in (
                    pygame.K_LEFT,
                    pygame.K_a
                ):

                    if direction != [CELL, 0]:

                        next_direction = [-CELL, 0]

                # RIGHT

                elif event.key in (
                    pygame.K_RIGHT,
                    pygame.K_d
                ):

                    if direction != [-CELL, 0]:

                        next_direction = [CELL, 0]


    # ==================================================
    # UPDATE GAME
    # ==================================================

    if not game_over and not paused:

        direction = next_direction

        # ----------------------------------------------
        # NEW HEAD
        # ----------------------------------------------

        new_head = [
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        ]

        snake.insert(0, new_head)

        # ----------------------------------------------
        # APPLE
        # ----------------------------------------------

        if snake[0] == apple:

            score += 10

            if score > high_score:

                high_score = score

            create_apple()

        else:

            snake.pop()

        # ----------------------------------------------
        # WALL COLLISION
        # ----------------------------------------------

        head = snake[0]

        if (
            head[0] < 0
            or head[0] >= WIDTH
            or head[1] < 0
            or head[1] >= HEIGHT
        ):

            game_over = True

        # ----------------------------------------------
        # SELF COLLISION
        # ----------------------------------------------

        if head in snake[1:]:

            game_over = True


    # ==================================================
    # DRAW
    # ==================================================

    draw_board()

    # Apple

    if not game_over:

        draw_apple()

    # Snake

    draw_snake()

    # ==================================================
    # SCORE
    # ==================================================

    score_text = font.render(
        f"Score: {score}",
        True,
        BLACK
    )

    best_text = font.render(
        f"Best: {high_score}",
        True,
        BLACK
    )

    screen.blit(
        score_text,
        (15, 12)
    )

    screen.blit(
        best_text,
        (15, 40)
    )

    # ==================================================
    # PAUSED
    # ==================================================

    if paused:

        pause_text = big_font.render(
            "PAUSED",
            True,
            BLACK
        )

        screen.blit(
            pause_text,
            (300, 250)
        )

        continue_text = font.render(
            "Press P to continue",
            True,
            BLACK
        )

        screen.blit(
            continue_text,
            (305, 320)
        )

    # ==================================================
    # GAME OVER
    # ==================================================

    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill(
            (255, 255, 255, 170)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            BLACK
        )

        screen.blit(
            game_over_text,
            (245, 220)
        )

        final_score = font.render(
            f"Score: {score}",
            True,
            BLACK
        )

        screen.blit(
            final_score,
            (350, 300)
        )

        restart_text = font.render(
            "Press R to restart",
            True,
            BLACK
        )

        screen.blit(
            restart_text,
            (315, 345)
        )

    # ==================================================
    # UPDATE SCREEN
    # ==================================================

    pygame.display.update()

    # ==================================================
    # CONSTANT SPEED
    # ==================================================

    clock.tick(10)


pygame.quit()