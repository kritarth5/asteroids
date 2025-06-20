import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialise pygame
    pygame.init()

    # initialise groups
    updateables = pygame.sprite.Group()
    drawables  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =  pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    shot.containers = (shots, updateables, drawables)
    
    # initialise objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # update player object
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")    
        updateables.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.collision(player_1):
                print("Game Over")
                sys.exit(1)
                
        # kill asteroids on impact
        for asteroid in asteroids:
            for shotter in shots:
                if asteroid.collision(shotter):
                    shotter.kill()
                    asteroid.split()


        
        # draw everything to screen
        for drawing in drawables:
            drawing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
            

if __name__ == "__main__":
    main()
