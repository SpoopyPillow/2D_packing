import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import numpy as np

from .circle import *


class CircleContainer:
    def __init__(self, radius, items):
        self.radius = radius
        self.items = items

    def draw(self):
        size = 800
        origin = [size / 2] * 2
        scale = (size / 2 - 100) / self.radius

        image = Image.new("RGB", (size, size))
        draw = ImageDraw.Draw(image)

        draw.ellipse(
            (
                origin[0] - self.radius * scale,
                origin[1] - self.radius * scale,
                origin[0] + self.radius * scale,
                origin[1] + self.radius * scale,
            )
        )

        for item in self.items:
            item.draw(draw, scale)

        return image

    def get_vector(self):
        return np.concatenate([item.get_vector() for item in self.items])

    def set_vector(self, vector):
        for i, item in enumerate(self.items):
            item.set_vector(vector[2 * i : 2 * i + 2])

    def fitness(self):
        penalty = 0
        for item_i in self.items:
            penalty += not item_i.is_contained(self)

            for item_j in self.items:
                if item_i == item_j:
                    continue
                penalty += item_i.is_overlapping(item_j)

        return 1 / (1 + penalty)
