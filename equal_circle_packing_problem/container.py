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

    def elastic_energy(self):
        total = 0
        for item_i in self.items:
            total += item_i.container_depth(self) ** 2
            
            for item_j in self.items:
                if (item_i == item_j):
                    continue
                total += item_i.circle_depth(item_j) ** 2

        return total
