import random
from equal_circle_packing_problem.circle import *
from equal_circle_packing_problem.container import *

container_size = 10
container = CircleContainer(
    container_size,
    [UnitCircle([random.randrange(-container_size, container_size) for j in range(2)]) for i in range(75)],
)
container.draw().show()

print(container.BFGS(0.1, 1000))
container.draw().show()
