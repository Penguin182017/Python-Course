import pygame
import random

pygame.init()

# ==================================================
# SETTINGS
# ==================================================

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐦 Flappy Bird")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 75)

# ==================================================
# COLORS
# ==================================================

SKY = (135, 206, 235)
GREEN = (70, 180, 70)
DARK_GREEN = (45, 140, 45)
YELLOW = (255, 220, 50)
ORANGE = (255, 150, 30)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GROUND = (220, 190, 90)

# ==================================================
# GAME SETTINGS
# ==================================================

GRAVITY = 0.5
FLAP_STRENGTH = -9

PIPE_WIDTH = 80
PIPE_GAP = 180

PIPE_SPEED = 4

# ==================================================
# BIRD
# ==================================================

bird_x = 150
bird_y = 300

bird_width = 40
bird_height = 30

bird_velocity = 0

# ==================================================
# GAME VARIABLES
# ==================================================

pipes = []

score = 0
high_score = 0

game_started = False
game_over = False

pipe_timer = 0

# ==================================================
# CREATE PIPE
# ==================================================

def create_pipe():

    gap_y = random.randint(
        150,
        HEIGHT - 180
    )

    top_height = gap_y - PIPE_GAP // 2

    bottom_y = gap_y + PIPE_GAP // 2

    top_pipe = pygame.Rect(
        WIDTH,
        0,
        PIPE_WIDTH,
        top_height
    )

    bottom_pipe = pygame.Rect(
        WIDTH,
        bottom_y,
        PIPE_WIDTH,
        HEIGHT - bottom_y
    )

    pipes.append({
        "top": top_pipe,
        "bottom": bottom_pipe,
        "passed": False
    })


# ==================================================
# RESET GAME
# ==================================================

def reset_game():

    global bird_y
    global bird_velocity
    global pipes
    global score
    global game_started
    global game_over
    global pipe_timer

    bird_y = 300

    bird_velocity = 0

    pipes = []

    score = 0

    game_started = False

    game_over = False

    pipe_timer = 0


# ==================================================
# DRAW BIRD
# ==================================================

def draw_bird():

    bird_rect = pygame.Rect(
        bird_x,
        int(bird_y),
        bird_width,
        bird_height
    )

    # Body

    pygame.draw.ellipse(
        screen,
        YELLOW,
        bird_rect
    )

    # Wing

    pygame.draw.ellipse(
        screen,
        ORANGE,
        (
            bird_x + 5,
            int(bird_y) + 15,
            20,
            10
        )
    )

    # Eye

    pygame.draw.circle(
        screen,
        WHITE,
        (
            bird_x + 28,
            int(bird_y) + 8
        ),
        6
    )

    pygame.draw.circle(
        screen,
        BLACK,
        (
            bird_x + 30,
            int(bird_y) + 8
        ),
        3
    )

    # Beak

    pygame.draw.polygon(
        screen,
        ORANGE,
        [
            (bird_x + 38, int(bird_y) + 12),
            (bird_x + 52, int(bird_y) + 17),
            (bird_x + 38, int(bird_y) + 21)
        ]
    )


# ==================================================
# DRAW PIPES
# ==================================================

def draw_pipes():

    for pipe in pipes:

        # Top pipe

        pygame.draw.rect(
            screen,
            GREEN,
            pipe["top"]
        )

        # Top pipe cap

        pygame.draw.rect(
            screen,
            DARK_GREEN,
            (
                pipe["top"].x - 5,
                pipe["top"].bottom - 20,
                PIPE_WIDTH + 10,
                20
            )
        )

        # Bottom pipe

        pygame.draw.rect(
            screen,
            GREEN,
            pipe["bottom"]
        )

        # Bottom pipe cap

        pygame.draw.rect(
            screen,
            DARK_GREEN,
            (
                pipe["bottom"].x - 5,
                pipe["bottom"].y,
                PIPE_WIDTH + 10,
                20
            )
        )


# ==================================================
# DRAW CLOUDS
# ==================================================

def draw_clouds():

    pygame.draw.circle(
        screen,
        WHITE,
        (150, 100),
        30
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (185, 100),
        40
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (225, 110),
        28
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (145, 105, 100, 30)
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (650, 160),
        25
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (680, 150),
        35
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (720, 160),
        25
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (645, 160, 100, 25)
    )


# ==================================================
# DRAW GROUND
# ==================================================

def draw_ground():

    pygame.draw.rect(
        screen,
        GROUND,
        (0, HEIGHT - 60, WIDTH, 60)
    )

    # Grass

    pygame.draw.rect(
        screen,
        GREEN,
        (0, HEIGHT - 60, WIDTH, 10)
    )


# ==================================================
# MAIN GAME
# ==================================================

running = True

reset_game()

while running:

    # ==================================================
    # EVENTS
    # ==================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            # ------------------------------------------
            # START / FLAP
            # ------------------------------------------

            if event.key in (
                pygame.K_SPACE,
                pygame.K_UP
            ):

                if not game_over:

                    game_started = True

                    bird_velocity = FLAP_STRENGTH

                else:

                    reset_game()

            # ------------------------------------------
            # RESTART
            # ------------------------------------------

            if event.key == pygame.K_r:

                reset_game()


    # ==================================================
    # GAME UPDATE
    # ==================================================

    if game_started and not game_over:

        # ----------------------------------------------
        # GRAVITY
        # ----------------------------------------------

        bird_velocity += GRAVITY

        bird_y += bird_velocity

        # ----------------------------------------------
        # CREATE PIPES
        # ----------------------------------------------

        pipe_timer += 1

        if pipe_timer >= 100:

            create_pipe()

            pipe_timer = 0

        # ----------------------------------------------
        # MOVE PIPES
        # ----------------------------------------------

        for pipe in pipes:

            pipe["top"].x -= PIPE_SPEED

            pipe["bottom"].x -= PIPE_SPEED

        # ----------------------------------------------
        # REMOVE OLD PIPES
        # ----------------------------------------------

        pipes = [
            pipe
            for pipe in pipes
            if pipe["top"].right > 0
        ]

        # ----------------------------------------------
        # BIRD RECT
        # ----------------------------------------------

        bird_rect = pygame.Rect(
            bird_x,
            int(bird_y),
            bird_width,
            bird_height
        )

        # ----------------------------------------------
        # PIPE COLLISION
        # ----------------------------------------------

        for pipe in pipes:

            if (
                bird_rect.colliderect(pipe["top"])
                or
                bird_rect.colliderect(pipe["bottom"])
            ):

                game_over = True

        # ----------------------------------------------
        # SCORE
        # ----------------------------------------------

        for pipe in pipes:

            if (
                not pipe["passed"]
                and pipe["top"].right < bird_x
            ):

                pipe["passed"] = True

                score += 1

                if score > high_score:

                    high_score = score

        # ----------------------------------------------
        # GROUND / SKY COLLISION
        # ----------------------------------------------

        if bird_y + bird_height >= HEIGHT - 60:

            game_over = True

        if bird_y <= 0:

            bird_y = 0

            bird_velocity = 0

    # ==================================================
    # DRAW
    # ==================================================

    screen.fill(SKY)

    draw_clouds()

    draw_pipes()

    draw_bird()

    draw_ground()

    # ==================================================
    # SCORE
    # ==================================================

    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    best_text = font.render(
        f"Best: {high_score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, 20)
    )

    screen.blit(
        best_text,
        (20, 60)
    )

    # ==================================================
    # START SCREEN
    # ==================================================

    if not game_started and not game_over:

        title = big_font.render(
            "FLAPPY BIRD",
            True,
            WHITE
        )

        instruction = font.render(
            "Press SPACE or UP to fly!",
            True,
            WHITE
        )

        screen.blit(
            title,
            (280, 220)
        )

        screen.blit(
            instruction,
            (280, 310)
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
            (0, 0, 0, 130)
        )

        screen.blit(
            overlay,
            (0, 0)
        )

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            WHITE
        )

        final_score = font.render(
            f"Score: {score}",
            True,
            WHITE
        )

        best_score = font.render(
            f"Best: {high_score}",
            True,
            WHITE
        )

        restart_text = font.render(
            "SPACE or R = Restart",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (300, 200)
        )

        screen.blit(
            final_score,
            (380, 290)
        )

        screen.blit(
            best_score,
            (380, 330)
        )

        screen.blit(
            restart_text,
            (320, 390)
        )

    # ==================================================
    # UPDATE
    # ==================================================

    pygame.display.update()

    clock.tick(60)


pygame.quit()