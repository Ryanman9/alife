import random

from .creature import Creature


class World:
    def __init__(self, width=50, height=50, n_creatures=100):
        self.width = width
        self.height = height
        self.tick_count = 0
        self.creatures = []

        for _ in range(n_creatures):
            c = Creature(
                x=random.uniform(0, width),
                y=random.uniform(0, height),
                speed=random.uniform(1.0, 4.0),
                vision=random.uniform(2.0, 8.0),
                energy=random.uniform(40.0, 60.0),
            )
            self.creatures.append(c)

    def tick(self):

        for c in self.creatures:
            c.tick(self)

        self.creatures = [c for c in self.creatures if c.alive]

        self.tick_count += 1

    def render_ascii(self):
        grid = [["." for _ in range(self.width)] for _ in range(self.height)]
        for c in self.creatures:
            gx = int(c.x)
            gy = int(c.y)
            if 0 <= gx < self.width and 0 <= gy < self.height:
                if c.speed < 2.0:
                    grid[gy][gx] = "s"
                elif c.speed < 3.0:
                    grid[gy][gx] = "C"
                else:
                    grid[gy][gx] = "F"
        return "\n".join("".join(row) for row in grid)
