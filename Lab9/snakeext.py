import pygame
import random
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
SNAKE_COLOR = (0, 128, 0)
FOOD_COLOR = (255, 0, 0)  # Food color is always red
BG_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 25
BASE_FOOD_LIFETIME = 30  # Base time in frames before food disappears

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the game speed
clock = pygame.time.Clock()

# Font for score display
font = pygame.font.SysFont('Arial', FONT_SIZE)

# Snake class (omitted for brevity)
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = SNAKE_COLOR
        self.score = 0
        self.level = 1
        self.apples_eaten = 0  # Initialize the apples eaten counter
    
    def eat_itself(self):
        return self.get_head_position() in self.positions[1:]


    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x * GRID_SIZE)) % SCREEN_WIDTH, (cur[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.level = 1
        self.apples_eaten = 0 #Reset apples counter

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


# Food class
class Food:
    def __init__(self, weight=1):
        self.position = (0, 0)
        self.color = FOOD_COLOR
        self.weight = weight
        self.lifetime = 0
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
        self.lifetime = 0

    def draw(self, surface):
        size = GRID_SIZE * self.weight
        r = pygame.Rect((self.position[0], self.position[1]), (size, size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def update(self, snake_level):
        self.lifetime += 1
        food_lifetime = BASE_FOOD_LIFETIME * snake_level
        if self.lifetime > food_lifetime:
            self.randomize_position()

# Main function
def main():
    snake = Snake()
    foods = [Food(weight=1), Food(weight=3)]  # List of different foods
    current_food = random.choice(foods)  # Start with a random food
    score = 0
    game_over = False

    while not game_over:
        clock.tick(10)
        snake.handle_keys()
        draw_grid(screen)
        snake.move()

        # Check for collisions with the walls or the snake's body
        if snake.get_head_position() == current_food.position:
            snake.length += current_food.weight
            current_food = random.choice(foods)  # Choose a new random food
            current_food.randomize_position()
            score += current_food.weight
            snake.apples_eaten += 1  # Increment the apples eaten counter
            if snake.apples_eaten % 3 == 0:
                snake.level += 1
                clock.tick(10 + snake.level)
        elif snake.get_head_position() in snake.positions[1:]:
            # Game over if the snake eats itself
            game_over = True
            score = 0  # Reset the score
            snake.apples_eaten = 0  # Reset the apples eaten counter

        current_food.update(snake.level)
        snake.draw(screen)
        current_food.draw(screen)
        draw_score(score, screen)
        pygame.display.update()

    # Game over screen
    screen.fill(BG_COLOR)
    game_over_text = font.render('Game Over!', True, FONT_COLOR)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.update()

    # Wait for a key press to reset the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                main()  # Recursively call main to reset the game
                return  # Exit the reset loop after resetting the game

# Draw grid function (omitted for brevity)
def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)


# Draw score function
def draw_score(score, surface):
    score_text = font.render(f'Score: {score}', True, FONT_COLOR)
    surface.blit(score_text, (10, 10))

# Run the game
if __name__ == "__main__":
    main()