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

    def step_inverse_hessian(self, inverse_hessian, position_step, gradient_step):
        inner_product = np.inner(gradient_step, position_step)

        return (
            np.identity(inverse_hessian.shape[0]) - np.outer(position_step, gradient_step) / inner_product
        ).dot(inverse_hessian).dot(
            np.identity(inverse_hessian.shape[0]) - np.outer(gradient_step, position_step) / inner_product
        ) + (
            np.outer(position_step, position_step) / inner_product
        )

    def BFGS(self, learning_rate, iterations):
        inverse_hessian = np.identity(2 * len(self.items))

        for iteration in range(iterations):
            gradient = self.gradient_energy()
            direction = -1 * inverse_hessian.dot(gradient)

            position_step = learning_rate * direction
            for index, item in enumerate(self.items):
                item.position += position_step[2 * index : 2 * index + 2]

            if np.linalg.norm(gradient) < 10**-10:
                return True

            gradient_step = self.gradient_energy() - gradient
            inverse_hessian = self.step_inverse_hessian(inverse_hessian, position_step, gradient_step)
        
        return False
