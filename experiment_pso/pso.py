import numpy as np
import copy

from .circle import *
from .container import *


class Particle:
    def __init__(self, container):
        self.container = container
        self.position = container.get_vector()
        self.velocity = np.random.rand(self.position.size)
        self.fitness = -1
        self.position_best = None
        self.fitness_best = -1

    def evaluate_fitness(self):
        self.fitness = self.container.fitness()

        if self.fitness > self.fitness_best:
            self.position_best = np.copy(self.position)
            self.fitness_best = self.fitness

    def update_velocity(self, position_global, inertial_constant, cognitive_constant, social_constant):
        cognitive_random = np.random.rand()
        social_random = np.random.rand()

        cognitive_velocity = cognitive_constant * cognitive_random * (self.position_best - self.position)
        social_velocity = social_constant * social_random * (position_global - self.position)

        self.velocity = inertial_constant * self.velocity + cognitive_velocity + social_velocity

    def update_position(self):
        self.position += self.velocity
        self.container.set_vector(self.position)
        for item in self.container.items:
            if not item.is_contained(self.container):
                item.position = np.array([0, 0], dtype=np.float64)
        self.position = self.container.get_vector()


def minimize(
    container,
    n_particles,
    max_iterations,
    inertial_max=0.9,
    inertial_min=0.4,
    cognitive_constant=1.5,
    social_constant=1.5,
):
    position_global = None
    fitness_global = -1

    swarm = []
    n_dim = container.get_vector().size
    for i in range(n_particles):
        new_container = copy.deepcopy(container)
        new_container.set_vector(np.random.rand(n_dim))
        swarm.append(Particle(new_container))

    for iteration in range(max_iterations):
        for particle in swarm:
            particle.evaluate_fitness()

            if particle.fitness > fitness_global:
                position_global = np.copy(particle.position)
                fitness_global = particle.fitness

                if fitness_global == 1.0:
                    return position_global, fitness_global

        inertial_constant = inertial_max - (inertial_max - inertial_min) * iteration / max_iterations
        for i, particle in enumerate(swarm):
            particle.update_velocity(position_global, inertial_constant, cognitive_constant, social_constant)
            particle.update_position()

            # if i == 1:
            #     print("ITERATION " + str(iteration))
            #     print(particle.velocity)

    return position_global, fitness_global
