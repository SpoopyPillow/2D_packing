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

    def total_energy(self):
        total = 0
        for i in range(len(self.items)):
            total += self.items[i].container_energy(self)

            for j in range(i + 1, len(self.items)):
                total += 2 * self.items[i].item_energy(self.items[j])

        return total

    def gradient_energy(self):
        partials = []
        for i in range(len(self.items)):
            partial = self.items[i].partial_container_energy(self)
            for j in range(len(self.items)):
                if i == j:
                    continue
                partial += self.items[i].partial_item_energy(self.items[j]) * 2

            partials.append(partial)

        return np.concatenate(partials)
