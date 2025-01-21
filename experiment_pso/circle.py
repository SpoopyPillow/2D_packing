import numpy as np


class UnitCircle:
    def __init__(self, position=[0, 0]):
        self.position = np.array(position, dtype=np.float64)

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
        
    def get_vector(self):
        return self.position
    
    def set_vector(self, vector):
        self.position = vector

    def is_contained(self, container):
        return np.linalg.norm(self.position) <= container.radius - 1

    def is_overlapping(self, circle):
        return np.linalg.norm(self.position - circle.position) < 2
