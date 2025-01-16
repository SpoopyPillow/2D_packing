import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

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
