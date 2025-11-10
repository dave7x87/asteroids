import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x),int(self.position.y)), int(self.radius), LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def _spawn_child(self, vel):
        child = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child.velocity = vel * 1.2
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        
        angle = random.uniform(20,50)
        
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        
        self._spawn_child(vector1)
        self._spawn_child(vector2)