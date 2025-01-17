import copy

from .container import *


class BasinHopping:
    def __init__(self, container, initial_shrink, hop_shrink, num_layouts):
        self.container = container
        self.initial_shrink = initial_shrink
        self.hop_shrink = hop_shrink
        self.num_layouts = num_layouts
        self.hops = 0

    def shrink_factor(self, layout):
        return (
            self.initial_shrink
            + self.hop_shrink * self.hops
            + (1 - self.initial_shrink - self.hop_shrink * self.hops) * layout / self.num_layouts
        )

    def generate_layouts(self, learning_rate, iterations):
        layouts = []
        for layout in range(self.num_layouts):
            shrinked_container = copy.copy(self.container)
            shrinked_container.radius *= self.shrink_factor(layout)
            shrinked_container.BFGS(learning_rate, iterations)
            shrinked_container.radius = self.container.radius
            shrinked_container.BFGS(learning_rate, iterations)

            layouts.append(shrinked_container)

        self.hops = (self.hops + 1) % int((1 - self.initial_shrink) / self.hop_shrink)
        return layouts
