import math
import random


class Creature:
    def __init__(self, x, y, speed=2.0, vision=5.0, energy=50.0):

        self.x = x
        self.y = y
        self.speed = speed
        self.vision = vision
        self.energy = energy
        self.age = 0
        self.generation = 0

    def tick(self, world):

        angle = random.uniform(0, 2 * math.pi)

        dx = math.cos(angle) * self.speed * 0.01
        dy = math.sin(angle) * self.speed * 0.01

        self.x += dx
        self.y += dy

        self.x = max(0, min(world.width - 1, self.x))
        self.y = max(0, min(world.height - 1, self.y))

        self.energy -= 0.05 * self.speed
        self.age += 1

    @property
    def alive(self):

        return self.energy > 0
