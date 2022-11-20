import exceptions
from test_V_creat import veh1, veh2, veh3, veh4

print('test-2. Метод start')
try:
    veh1.start()
except exceptions.LowFuelError as LFE:
    print(f'{veh1} - {LFE}')
else:
    print(f'{veh1}')

try:
    veh2.start()
except exceptions.LowFuelError as LFE:
    print(f'{veh2} - {LFE}')
else:
    print(f'{veh2}')

try:
    veh3.start()
except exceptions.LowFuelError as LFE:
    print(f'{veh3} - {LFE}')
else:
    print(f'{veh3}')

try:
    veh4.start()
except exceptions.LowFuelError as LFE:
    print(f'{veh4} - {LFE}')
else:
    print(f'{veh4}')

