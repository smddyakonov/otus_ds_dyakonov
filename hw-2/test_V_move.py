import exceptions
from test_V_creat import veh1, veh2, veh3, veh4

print('test-3. Метод move')
try:
    veh1.move()
except exceptions.NotEnoughFuel as NEF:
    print(f'{veh1} - {NEF}')
else:
    print(f'{veh1}')

try:
    veh2.move()
except exceptions.NotEnoughFuel as NEF:
    print(f'{veh2} - {NEF}')
else:
    print(f'{veh2}')

try:
    veh3.move()
except exceptions.NotEnoughFuel as NEF:
    print(f'{veh3} - {NEF}')
else:
    print(f'{veh3}')

for _ in range(11):
    try:
        veh4.move()
    except exceptions.NotEnoughFuel as NEF:
        print(f'{veh4} - {NEF}')
    else:
        print(f'{veh4}')
