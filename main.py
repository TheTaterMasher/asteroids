import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroidField = AsteroidField()

    # Game loop
    while True:
        # check if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        for object in updateable:
            object.update(dt)

        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game Over!")
                return
            
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()


        # draw
        screen.fill("black")

        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()


        # increment clock, dt is time in seconds per frame (about 0.016s)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()