import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


# make a class for shooting
class shot(CircleShape):
    def __init__(self,x,y,radius=SHOT_RADIUS):
        self.radius = radius
        super().__init__(x,y,radius)

    def draw(self, screen):
        self.asteroid = pygame.draw.circle(screen,"white",center = (self.position.x, self.position.y), radius = self.radius , width = 2)

    def update(self, dt):
        self.position += self.velocity * dt



