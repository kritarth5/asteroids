from constants import ASTEROID_MIN_RADIUS
from player import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        self.asteroid = pygame.draw.circle(screen,"white",center = (self.position.x, self.position.y), radius = self.radius , width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # if asteroid split into smaller one, destroy asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # If not, check where the radius lies and make three kinds of splits
        else:
            angle = random.uniform(20,50)
            velocity_a = self.velocity.rotate(angle)
            velocity_b = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = velocity_a*1.2
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b.velocity = velocity_b*1.2            
            

        
