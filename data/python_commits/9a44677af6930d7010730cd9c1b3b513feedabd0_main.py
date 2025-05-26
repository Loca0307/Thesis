import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen and clock
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake settings
BLOCK_SIZE = 20

# Directions
UP = (0, -BLOCK_SIZE)
DOWN = (0, BLOCK_SIZE)
LEFT = (-BLOCK_SIZE, 0)
RIGHT = (BLOCK_SIZE, 0)

# Font for displaying score and game over message
font = pygame.font.SysFont(None, 35)

# Function to display score
def display_score(player_score, ai_score):
    score_text = font.render(f"Player: {player_score}  AI: {ai_score}", True, WHITE)
    screen.blit(score_text, [10, 10])

# Function to display the game over message
def display_game_over(winner, message):
    game_over_text = font.render(f"Game Over! {winner} Wins!", True, WHITE)
    explanation_text = font.render(message, True, WHITE)
    screen.blit(game_over_text, [WIDTH // 4, HEIGHT // 2])
    screen.blit(explanation_text, [WIDTH // 4, HEIGHT // 2 + 30])

# Snake class
class Snake:
    def __init__(self, color, start_pos, direction):
        self.color = color
        self.body = [start_pos]
        self.direction = direction
        self.score = 0
    
    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x) % WIDTH, (head_y + dir_y) % HEIGHT
        self.body = [new_head] + self.body[:-1]
    
    def grow(self):
        self.body.append(self.body[-1])
    
    def check_collision(self):
        head = self.body[0]
        # Check if head collides with its own body
        if head in self.body[1:]:
            return True
        return False
    
    def check_collision_with_other_snake(self, other_snake):
        head = self.body[0]
        # Check if head collides with the other snake's body
        if head in other_snake.body[1:]:
            return True
        return False
    
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# AI Snake class
class AISnake(Snake):
    def __init__(self, color, start_pos, direction):
        super().__init__(color, start_pos, direction)
    
    def move_towards_food(self, food_pos):
        head_x, head_y = self.body[0]
        food_x, food_y = food_pos

        # AI logic to move towards food, avoiding boundaries
        if food_x > head_x:
            self.direction = RIGHT
        elif food_x < head_x:
            self.direction = LEFT
        if food_y > head_y:
            self.direction = DOWN
        elif food_y < head_y:
            self.direction = UP

    def update(self, food_pos):
        self.move_towards_food(food_pos)
        self.move()

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
    
    def spawn(self):
        self.position = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# Game loop
def game_loop():
    player = Snake(GREEN, (100, 100), RIGHT)
    ai = AISnake(BLUE, (300, 300), LEFT)
    food = Food()
    
    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Change direction immediately without waiting for snake movement
                if event.key == pygame.K_UP and player.direction != DOWN:
                    player.direction = UP
                elif event.key == pygame.K_DOWN and player.direction != UP:
                    player.direction = DOWN
                elif event.key == pygame.K_LEFT and player.direction != RIGHT:
                    player.direction = LEFT
                elif event.key == pygame.K_RIGHT and player.direction != LEFT:
                    player.direction = RIGHT
        
        # Move the snakes
        player.move()
        ai.update(food.position)  # Update AI with new direction and move
        
        # Check for collisions
        if player.check_collision():
            winner = "AI"
            message = "Player collided with their own body."
            display_game_over(winner, message)
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds to display the game over message
            running = False
        elif ai.check_collision():
            winner = "Player"
            message = "AI collided with its own body."
            display_game_over(winner, message)
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds to display the game over message
            running = False
        
        # Check if the player or AI hits the other snake's body
        elif player.check_collision_with_other_snake(ai):
            winner = "AI"
            message = "Player collided with AI's body."
            display_game_over(winner, message)
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds to display the game over message
            running = False
        elif ai.check_collision_with_other_snake(player):
            winner = "Player"
            message = "AI collided with Player's body."
            display_game_over(winner, message)
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds to display the game over message
            running = False
        
        # Check if the player or AI eats the food
        if player.body[0] == food.position:
            player.grow()
            player.score += 1
            food.spawn()
        if ai.body[0] == food.position:
            ai.grow()
            ai.score += 1
            food.spawn()
        
        # Draw everything
        player.draw(screen)
        ai.draw(screen)
        food.draw(screen)
        display_score(player.score, ai.score)
        
        # Update the display
        pygame.display.flip()
        clock.tick(10)  # Slow game speed for a relaxed experience
    
    # End of game
    pygame.quit()

# Run the game
game_loop()