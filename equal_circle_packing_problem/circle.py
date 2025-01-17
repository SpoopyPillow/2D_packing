import math
import numpy as np


class UnitCircle:
    def __init__(self, position=[0, 0]):
        self.position = position

    def draw(self, draw, scale):
        origin = (draw.im.size[0] / 2, draw.im.size[1] / 2)
        draw.ellipse(
            (
                origin[0] + (self.position[0] - 1) * scale,
                origin[1] - (self.position[1] + 1) * scale,
                origin[0] + (self.position[0] + 1) * scale,
                origin[1] - (self.position[1] - 1) * scale,
            )
        )

    def container_energy(self, container):
        return max(math.dist([0, 0], self.position) + 1 - container.radius, 0) ** 2

    def partial_container_energy(self, container):
        if self.container_energy(container) == 0:
            return np.zeros(2)

        x = self.position[0]
        y = self.position[1]

        return np.array(
            [
                2 * x + 2 * (1 - container.radius) * x / math.sqrt(x**2 + y**2),
                2 * y + 2 * (1 - container.radius) * y / math.sqrt(x**2 + y**2),
            ]
        )

    def item_energy(self, item):
        return max(2 - math.dist(self.position, item.position), 0) ** 2

    def partial_item_energy(self, item):
        if self.position == item.position or self.item_energy(item) == 0:
            return np.zeros(2)

        x = self.position[0]
        y = self.position[1]
        item_x = item.position[0]
        item_y = item.position[1]

        return np.array(
            [
                2 * (x - item_x) - 4 * (x - item_x) / math.sqrt((x - item_x) ** 2 + (y - item_y) ** 2),
                2 * (y - item_y) - 4 * (y - item_y) / math.sqrt((x - item_x) ** 2 + (y - item_y) ** 2),
            ]
        )
