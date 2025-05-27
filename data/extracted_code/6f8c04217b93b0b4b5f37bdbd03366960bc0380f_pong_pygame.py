import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Casse")

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Police
font = pygame.font.Font(None, 36)


# Fonction pour afficher un bouton (Rejouer)
def draw_button():
    pygame.draw.rect(screen, RED, (WIDTH // 2 - 75, HEIGHT // 2, 150, 50))
    text = font.render("Rejouer", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 40, HEIGHT // 2 + 10))


# Fonction pour afficher un écran de fin (victoire ou game over)
def show_end_screen(message):
    screen.fill(BLACK)
    text = font.render(message, True, WHITE)
    screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2 - 50))
    draw_button()
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH // 2 - 75 <= x <= WIDTH // 2 + 75 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
                    return True
    return False


# Fonction principale du jeu
def game_loop():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, bar_x, bricks

    # Réinitialisation des variables du jeu
    ball_x, ball_y = WIDTH // 2, HEIGHT - 50
    ball_speed_x, ball_speed_y = random.choice([-3, 3]), -3
    bar_x = WIDTH // 2 - 50

    # Création des briques
    bricks = [pygame.Rect(col * 70 + 35, row * 25 + 40, 60, 20) for row in range(5) for col in range(10)]

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Déplacement de la barre
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bar_x > 0:
            bar_x -= 6
        if keys[pygame.K_RIGHT] and bar_x < WIDTH - 100:
            bar_x += 6

        # Déplacement de la balle
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Collision avec les murs
        if ball_x - 10 <= 0 or ball_x + 10 >= WIDTH:
            ball_speed_x = -ball_speed_x
        if ball_y - 10 <= 0:
            ball_speed_y = -ball_speed_y
        if ball_y + 10 >= HEIGHT:
            run = False  # Game over si la balle touche le bas

        # Collision avec la barre
        bar_rect = pygame.Rect(bar_x, HEIGHT - 30, 100, 20)
        ball_rect = pygame.Rect(ball_x - 10, ball_y - 10, 20, 20)
        if ball_rect.colliderect(bar_rect):
            ball_speed_y = -abs(ball_speed_y)
            ball_speed_x += random.choice([-1, 1])  # Effet de variation du rebond

        # Collision avec les briques
        for brick in bricks[:]:
            if ball_rect.colliderect(brick):
                bricks.remove(brick)
                ball_speed_y = -ball_speed_y
                break

        # Vérifier si toutes les briques sont détruites
        if not bricks:
            run = False
            victory = True  # Indique qu'on a gagné

        # Dessiner les éléments du jeu
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)
        pygame.draw.rect(screen, BLUE, (bar_x, HEIGHT - 30, 100, 20))
        for brick in bricks:
            pygame.draw.rect(screen, GREEN, brick)

        pygame.display.update()

    # Affichage de l'écran de fin (victoire ou game over)
    if not bricks:
        message = "Victoire !"
    else:
        message = "Game Over"

    if show_end_screen(message):
        game_loop()  # Relancer une partie


# Lancer le jeu
game_loop()