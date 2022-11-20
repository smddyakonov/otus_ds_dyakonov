import Plane
import exceptions

print('test-5. Plane')

plane1 = Plane.Plane('pln1', max_cargo=10)
try:
    plane1.load_cargo(5)
except exceptions.CargoOverload as COL:
    print(COL)
try:
    for _ in range(5):
        plane1.load_cargo(5)
        print(plane1.cargo)
        print(plane1.max_cargo)
except exceptions.CargoOverload as COL:
    print(COL)

print(plane1.cargo)

plane1.remove_all_cargo()

print(plane1.cargo)