import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
WHITE = (255, 255, 255)
FPS = 60

# Setup the display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Tank Simulator")

# Fish class
class Fish:
    def __init__(self):
        self.x = random.randint(50, WIDTH-50)
        self.y = random.randint(50, HEIGHT-50)
        self.size = random.randint(10, 20)
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])
        self.target = None

    def move(self):
        if self.target:
            target_x, target_y = self.target.x, self.target.y
            if self.x < target_x:
                self.x += 1
            elif self.x > target_x:
                self.x -= 1
            if self.y < target_y:
                self.y += 1
            elif self.y > target_y:
                self.y -= 1

            # Check if reached the target
            if abs(self.x - target_x) < 5 and abs(self.y - target_y) < 5:
                self.target = None
        else:
            self.x += self.speed_x
            self.y += self.speed_y

        # Bounce off the edges
        if self.x < 0 or self.x > WIDTH:
            self.speed_x *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.ellipse(window, BLUE, (self.x, self.y, self.size*2, self.size))

# Plant class
class Plant:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT

    def draw(self):
        pygame.draw.rect(window, BLUE, (self.x, self.y-100, 10, 100))

# Food class
class Food:
    def __init__(self):
        self.x = random.randint(50, WIDTH-50)
        self.y = 0

    def move(self):
        self.y += 2

    def draw(self):
        pygame.draw.circle(window, WHITE, (self.x, int(self.y)), 5)

# Initialize fish, plants, and food
fishes = [Fish() for _ in range(6)]
plants = [Plant(x) for x in range(100, WIDTH, 150)]
food_drops = []

clock = pygame.time.Clock()
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_food = Food()
                food_drops.append(new_food)
                for fish in fishes:
                    fish.target = new_food

    # Logic
    for fish in fishes:
        fish.move()
    for food in food_drops:
        food.move()

    # Draw everything
    window.fill(BLACK)
    for plant in plants:
        plant.draw()
    for fish in fishes:
        fish.draw()
    for food in food_drops:
        food.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
