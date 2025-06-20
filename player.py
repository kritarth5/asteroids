from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import shot

class Player(CircleShape):
    """ Make a player object for asteriods """
    def __init__(self,x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.delay = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        self.player = pygame.draw.polygon(screen,"white",self.triangle(),width=2)
        
    def rotate(self, dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED*dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.delay <= 0:
            shota = shot(self.position.x, self.position.y)
            shota.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.delay = PLAYER_SHOOT_COOLDOWN
        else:
            pass
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
           self.shoot()

        # reduce delay timer
        self.delay -= dt
