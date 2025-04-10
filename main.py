import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group() 
    
    Player.containers = (updatable, drawable) #pyright: ignore
    Asteroid.containers = (asteroids,updatable,drawable) #pyright: ignore
    AsteroidField.containers = (updatable) #pyright: ignore
    Shot.containers = (shots,updatable,drawable) #pyright: ignore
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

       
        updatable.update(dt)
        screen.fill("black")
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                return
        
        for sprite in drawable:
            sprite.draw(screen)
      
            
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

