from equal_circle_packing_problem.circle import *
from equal_circle_packing_problem.container import *


a = UnitCircle([10, 0])
b = UnitCircle([9.5, 0.5])
c = UnitCircle([0.5, -0.5])

container = CircleContainer(10, [a, b, c])
container.draw().show()

print(container.total_energy())
print(container.gradient_energy())
