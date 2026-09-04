import pygame
import random

pygame.init()

# ==================================================
# SETTINGS
# ==================================================

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penguin Adventure - 10 Levels")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 65)

# ==================================================
# PLAYER
# ==================================================

player = pygame.Rect(100, 300, 40, 50)

player_speed = 10

health = 100
score = 0
level = 1

# ==================================================
# ENEMY SPEED
# ==================================================

enemy_speed = 1.0

# ==================================================
# GAME OBJECTS
# ==================================================

fish = []
enemies = []
walls = []
chests = []

# ==================================================
# BOSS
# ==================================================

boss = pygame.Rect(720, 250, 90, 90)

boss_x = 720.0
boss_y = 250.0

boss_speed = 2.0
boss_health = 150

# ==================================================
# GAME STATE
# ==================================================

running = True
game_won = False


# ==================================================
# CREATE LEVEL
# ==================================================

def create_level():

    global enemy_speed

    fish.clear()
    enemies.clear()
    walls.clear()
    chests.clear()

    # Enemy gets faster every level
   
    # ==================================================
    # ICE WALLS
    # ==================================================

    walls.extend([
        pygame.Rect(200, 100, 300, 25),
        pygame.Rect(200, 475, 300, 25),
        pygame.Rect(600, 150, 25, 300)
    ])

    # ==================================================
    # FISH
    # ==================================================

    fish_amount = 5 + level

    for i in range(fish_amount):

        while True:

            x = random.randint(50, 820)
            y = random.randint(60, 520)

            new_fish = pygame.Rect(
                x,
                y,
                20,
                20
            )

            touching_wall = False

            for wall in walls:

                if new_fish.colliderect(wall):

                    touching_wall = True
                    break

            if not touching_wall:

                fish.append(new_fish)
                break

    # ==================================================
    # ENEMIES
    # ==================================================

    enemy_amount = 1 + level

    for i in range(enemy_amount):

        x = random.randint(400, 820)
        y = random.randint(80, 500)

        enemy = {
            "rect": pygame.Rect(x, y, 40, 40),
            "x": float(x),
            "y": float(y),
            "health": 3
        }

        enemies.append(enemy)

    # ==================================================
    # TREASURE
    # ==================================================

    chest_amount = 1 + level // 3

    for i in range(chest_amount):

        while True:

            x = random.randint(80, 800)
            y = random.randint(80, 500)

            new_chest = pygame.Rect(
                x,
                y,
                35,
                30
            )

            touching_wall = False

            for wall in walls:

                if new_chest.colliderect(wall):

                    touching_wall = True
                    break

            if not touching_wall:

                chests.append(new_chest)
                break


# ==================================================
# RESTART GAME
# ==================================================

def restart_game():

    global health
    global score
    global level
    global boss_health
    global boss_x
    global boss_y
    global game_won

    health = 100
    score = 0
    level = 1

    boss_health = 150

    boss_x = 720.0
    boss_y = 250.0

    boss.x = 720
    boss.y = 250

    player.x = 100
    player.y = 300

    game_won = False

    create_level()


# ==================================================
# START
# ==================================================

create_level()


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

    # ==================================================
    # LEVELS 1 - 9
    # ==================================================

    if level < 10 and not game_won and health > 0:

        keys = pygame.key.get_pressed()

        old_position = player.copy()

        # ==================================================
        # PLAYER MOVEMENT
        # ==================================================

        if keys[pygame.K_LEFT]:
            player.x -= player_speed

        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        if keys[pygame.K_UP]:
            player.y -= player_speed

        if keys[pygame.K_DOWN]:
            player.y += player_speed

        # ==================================================
        # WALL COLLISION
        # ==================================================

        for wall in walls:

            if player.colliderect(wall):

                player = old_position

        # ==================================================
        # SCREEN BOUNDARIES
        # ==================================================

        player.x = max(
            0,
            min(WIDTH - player.width, player.x)
        )

        player.y = max(
            0,
            min(HEIGHT - player.height, player.y)
        )

        # ==================================================
        # FISH
        # ==================================================

        for f in fish[:]:

            if player.colliderect(f):

                fish.remove(f)

                score += 10

        # ==================================================
        # TREASURE
        # ==================================================

        for chest in chests[:]:

            if player.colliderect(chest):

                chests.remove(chest)

                score += 50

        # ==================================================
        # ENEMIES
        # ==================================================

        for enemy in enemies[:]:

            # Move toward player

            if enemy["x"] < player.x:
                enemy["x"] += enemy_speed

            elif enemy["x"] > player.x:
                enemy["x"] -= enemy_speed

            if enemy["y"] < player.y:
                enemy["y"] += enemy_speed

            elif enemy["y"] > player.y:
                enemy["y"] -= enemy_speed

            # Update rectangle

            enemy["rect"].x = round(enemy["x"])
            enemy["rect"].y = round(enemy["y"])

            # Enemy damages player

            if player.colliderect(enemy["rect"]):

                health -= 1

        # ==================================================
        # ATTACK ENEMIES
        # ==================================================

        if keys[pygame.K_SPACE]:

            attack = pygame.Rect(
                player.x - 30,
                player.y - 30,
                100,
                110
            )

            for enemy in enemies[:]:

                if attack.colliderect(enemy["rect"]):

                    enemy["health"] -= 1

                    if enemy["health"] <= 0:

                        enemies.remove(enemy)

                        score += 25

        # ==================================================
        # LEVEL COMPLETE
        # ==================================================

        if len(fish) == 0:

            level += 1

            if level < 10:

                player.x = 100
                player.y = 300

                create_level()

            else:

                # Start boss level

                player.x = 100
                player.y = 300

                enemies.clear()
                fish.clear()
                chests.clear()

    # ==================================================
    # LEVEL 10 BOSS
    # ==================================================

    elif level == 10 and not game_won and health > 0:

        keys = pygame.key.get_pressed()

        # ==================================================
        # PLAYER MOVEMENT
        # ==================================================

        if keys[pygame.K_LEFT]:
            player.x -= player_speed

        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        if keys[pygame.K_UP]:
            player.y -= player_speed

        if keys[pygame.K_DOWN]:
            player.y += player_speed

        # ==================================================
        # SCREEN BOUNDARIES
        # ==================================================

        player.x = max(
            0,
            min(WIDTH - player.width, player.x)
        )

        player.y = max(
            0,
            min(HEIGHT - player.height, player.y)
        )

        # ==================================================
        # BOSS MOVEMENT
        # ==================================================

        if boss_x < player.x:
            boss_x += boss_speed

        elif boss_x > player.x:
            boss_x -= boss_speed

        if boss_y < player.y:
            boss_y += boss_speed

        elif boss_y > player.y:
            boss_y -= boss_speed

        boss.x = round(boss_x)
        boss.y = round(boss_y)

        # ==================================================
        # BOSS DAMAGE
        # ==================================================

        if player.colliderect(boss):

            health -= 1

        # ==================================================
        # ATTACK BOSS
        # ==================================================

        if keys[pygame.K_SPACE]:

            attack = pygame.Rect(
                player.x - 30,
                player.y - 30,
                100,
                110
            )

            if attack.colliderect(boss):

                boss_health -= 1

        # ==================================================
        # BOSS DEFEATED
        # ==================================================

        if boss_health <= 0:

            game_won = True

    # ==================================================
    # WIN SCREEN
    # ==================================================

    if game_won:

        screen.fill(
            (30, 160, 90)
        )

        win_text = big_font.render(
            "YOU WON!",
            True,
            (255, 255, 255)
        )

        final_text = font.render(
            f"Final Score: {score}",
            True,
            (255, 255, 255)
        )

        boss_text = font.render(
            "You defeated the Level 10 Boss!",
            True,
            (255, 255, 255)
        )

        restart_text = font.render(
            "Press R to Play Again",
            True,
            (255, 255, 255)
        )

        screen.blit(win_text, (300, 190))
        screen.blit(final_text, (350, 280))
        screen.blit(boss_text, (280, 330))
        screen.blit(restart_text, (320, 390))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:

            restart_game()

    # ==================================================
    # GAME OVER
    # ==================================================

    elif health <= 0:

        screen.fill(
            (30, 30, 30)
        )

        game_over = big_font.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )

        score_text = font.render(
            f"Score: {score}",
            True,
            (255, 255, 255)
        )

        restart_text = font.render(
            "Press R to Restart",
            True,
            (255, 255, 255)
        )

        screen.blit(game_over, (280, 200))
        screen.blit(score_text, (390, 290))
        screen.blit(restart_text, (330, 340))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:

            restart_game()

    # ==================================================
    # NORMAL GAME DRAW
    # ==================================================

    else:

        screen.fill(
            (150, 210, 255)
        )

        # ==================================================
        # ICE WALLS
        # ==================================================

        for wall in walls:

            pygame.draw.rect(
                screen,
                (220, 245, 255),
                wall
            )

        # ==================================================
        # FISH
        # ==================================================

        for f in fish:

            pygame.draw.circle(
                screen,
                (255, 180, 40),
                f.center,
                10
            )

        # ==================================================
        # TREASURE
        # ==================================================

        for chest in chests:

            pygame.draw.rect(
                screen,
                (180, 120, 40),
                chest
            )

        # ==================================================
        # ENEMIES
        # ==================================================

        for enemy in enemies:

            pygame.draw.rect(
                screen,
                (180, 40, 40),
                enemy["rect"]
            )

            # Enemy HP bar

            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    enemy["rect"].x,
                    enemy["rect"].y - 10,
                    40,
                    5
                )
            )

            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (
                    enemy["rect"].x,
                    enemy["rect"].y - 10,
                    40 * enemy["health"] / 3,
                    5
                )
            )

        # ==================================================
        # PENGUIN
        # ==================================================

        pygame.draw.ellipse(
            screen,
            (30, 30, 40),
            player
        )

        # Belly

        pygame.draw.ellipse(
            screen,
            (240, 240, 240),
            (
                player.x + 7,
                player.y + 15,
                26,
                30
            )
        )

        # Eyes

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                player.x + 12,
                player.y + 13
            ),
            5
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (
                player.x + 28,
                player.y + 13
            ),
            5
        )

        # ==================================================
        # FINAL BOSS
        # ==================================================

        if level == 10:

            pygame.draw.rect(
                screen,
                (150, 30, 30),
                boss
            )

            # Boss HP background

            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    600,
                    40,
                    250,
                    25
                )
            )

            # Boss HP

            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (
                    600,
                    40,
                    max(
                        0,
                        boss_health / 150 * 250
                    ),
                    25
                )
            )

            boss_text = font.render(
                f"FINAL BOSS HP: {boss_health}",
                True,
                (255, 255, 255)
            )

            screen.blit(
                boss_text,
                (600, 5)
            )

            attack_text = font.render(
                "SPACE = ATTACK",
                True,
                (255, 255, 255)
            )

            screen.blit(
                attack_text,
                (650, 80)
            )

        # ==================================================
        # UI
        # ==================================================

        score_text = font.render(
            f"Score: {score}",
            True,
            (0, 0, 0)
        )

        health_text = font.render(
            f"Health: {health}",
            True,
            (0, 0, 0)
        )

        level_text = font.render(
            f"Level: {level}/10",
            True,
            (0, 0, 0)
        )

        speed_text = font.render(
            f"Enemy Speed: {enemy_speed:.1f}",
            True,
            (0, 0, 0)
        )

        attack_help = font.render(
            "SPACE = ATTACK",
            True,
            (0, 0, 0)
        )

        screen.blit(score_text, (20, 20))
        screen.blit(health_text, (20, 55))
        screen.blit(level_text, (20, 90))
        screen.blit(speed_text, (20, 125))
        screen.blit(attack_help, (20, 160))

    # ==================================================
    # UPDATE SCREEN
    # ==================================================

    pygame.display.update()

    clock.tick(60)


pygame.quit()