"""
This is a simple particle system that creates particles
at the center of the screen and moves them in random directions.
The particles will slowly shrink and disappear after a while.
"""

import random
import math
import pygame

class Particle:
    """
    A single particle in the particle system.
    """
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = random.uniform(1, 3)
        self.angle = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.size *= 0.99  # particles will slowly shrink

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class ParticleSystem:
    """
    A simple particle system that creates and manages particles.
    """
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y, size, color):
        """
        Add a new particle to the system.
        """
        self.particles.append(Particle(x, y, size, color))

    def update(self, screen):
        """
        Update and draw all particles in the system.
        """
        for particle in self.particles[:]:
            particle.move()
            particle.draw(screen)
            if particle.size < 0.5:
                self.particles.remove(particle)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    ps = ParticleSystem()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((0, 0, 0))
        ps.add_particle(400, 300, 10, (255, 255, 255))
        ps.update(screen)
        pygame.display.flip()
        clock.tick(60)