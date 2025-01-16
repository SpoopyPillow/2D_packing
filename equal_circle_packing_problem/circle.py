import math


class UnitCircle:
    def __init__(self, position=[0, 0]):
        self.position = position

    def draw(self, draw, scale):
        origin = (draw.im.size[0] / 2, draw.im.size[1] / 2)
        draw.ellipse(
            (
                origin[0] + (self.position[0] - 1) * scale,
                origin[1] + (self.position[1] - 1) * scale,
                origin[0] + (self.position[0] + 1) * scale,
                origin[1] + (self.position[1] + 1) * scale,
            )
        )

    def circle_depth(self, circle):
        return max(2 - math.dist(self.position, circle.position), 0)

    def container_depth(self, container):
        return max(math.dist([0, 0], self.position) + 1 - container.radius, 0)
