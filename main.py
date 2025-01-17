import random
from equal_circle_packing_problem.circle import *
from equal_circle_packing_problem.container import *
from equal_circle_packing_problem.basin_hopping import *

container_size = 3.8
container = CircleContainer(
    container_size,
    [UnitCircle([random.uniform(-container_size, container_size) for j in range(2)]) for i in range(10)],
)

container.BFGS(0.1, 100)
container.draw().show()

basin_hopping = BasinHopping(container, 0.4, 0.03, 10)
layouts = basin_hopping.generate_layouts(0.1, 100)

optimized = min(layouts, key=lambda container: container.total_energy())
optimized.draw().show()