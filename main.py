import random
from experiment_pso.circle import *
from experiment_pso.container import *
from experiment_pso.pso import *

container_size = 3
container = CircleContainer(
    container_size,
    [UnitCircle([0, 0]) for i in range(4)],
)

position_global, fitness_global = minimize(container, 200, 1000, 0.9, 0.4, 1.5, 1.5)
container.set_vector(position_global)
print(fitness_global)
print(container.fitness())
container.draw().show()
