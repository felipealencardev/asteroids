import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        pygame.Surface.fill(screen, BACKGROUND_COLOR)

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
