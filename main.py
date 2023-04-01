import pygame
import random


pygame.init()
WIDTH = 500
HEIGHT = 500
FPS = 10
GRID_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
class Snake:
    def __init__(self):
        self.segments = [(WIDTH/2, HEIGHT/2)]
        self.direction = random.choice(['up', 'down', 'left', 'right'])
    def move(self):
        x, y = self.segments[0]
        if self.direction == 'up':
            y -= GRID_SIZE
        elif self.direction == 'down':
            y += GRID_SIZE
        elif self.direction == 'left':
            x -= GRID_SIZE
        elif self.direction == 'right':
            x += GRID_SIZE
        self.segments.insert(0, (x, y))
        self.segments.pop()
    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    def grow(self):
        x, y = self.segments[-1]
        if self.direction == 'up':
            y += GRID_SIZE
        elif self.direction == 'down':
            y -= GRID_SIZE
        elif self.direction == 'left':
            x += GRID_SIZE
        elif self.direction == 'right':
            x -= GRID_SIZE
        self.segments.append((x, y))
    def check_collision(self):
        x, y = self.segments[0]
        if x < 0 or x > WIDTH - GRID_SIZE or y < 0 or y > HEIGHT - GRID_SIZE:
            return True
        for segment in self.segments[1:]:
            if x == segment[0] and y == segment[1]:
                return True
        return False
    def change_direction(self, direction):
        if direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif direction == 'right' and self.direction != 'left':
            self.direction = 'right'
class Food:
    def __init__(self):
        self.position = self.randomize_position()
    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
    def randomize_position(self):
        x = random.randrange(0, WIDTH-GRID_SIZE, GRID_SIZE)
        y = random.randrange(0, HEIGHT-GRID_SIZE, GRID_SIZE)
        return (x, y)
snake = Snake()
food = Food()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('right')
    snake.move()
    if snake.check_collision():
        running = False
    if snake.segments[0] == food.position:
        snake.grow()
        food.position = food.randomize_position()
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()
pygame.quit()