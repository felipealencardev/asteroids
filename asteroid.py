import pygame
import random

from circleshape import CircleShape
from constants import (
    OBJ_COLOR, 
    OBJ_LINE_WIDTH, 
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPLIT_SPEED
)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, OBJ_COLOR, self.position, self.radius, OBJ_LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * ASTEROID_SPLIT_SPEED
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * ASTEROID_SPLIT_SPEED