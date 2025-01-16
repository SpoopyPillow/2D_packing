from equal_circle_packing_problem.circle import *
from equal_circle_packing_problem.container import *

container = CircleContainer(10, [UnitCircle([2, 0])])
container.draw().show()

print(container.elastic_energy())