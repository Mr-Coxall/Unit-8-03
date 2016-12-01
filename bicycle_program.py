# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This main program will create a bicycle object

from bicycle import *

# create an instance of a bicycle
bike1 = Bicycle()
bike2 = Bicycle()

print('New bike1')
print('Set cadence to 40')
bike1.set_cadence(40)
print('Current speed: ' + str(bike1.get_speed()))
print('Set gear to 7')
bike1.set_gear(7)
print('Current gear: ' + str(bike1.get_gear()))
print('Current speed: ' + str(bike1.get_speed()))
print('Set cadence to 60')
bike1.set_cadence(60)
print('Current cadence: ' + str(bike1.get_cadence()))
print('Current speed: ' + str(bike1.get_speed()))
print('Apply breaks by 3')
bike1.apply_brakes(3)
print('Current speed: ' + str(bike1.get_speed()))

print('')

print('New bike2')
print('Set cadence to 40')
bike2.set_cadence(90)
print('Current speed: ' + str(bike2.get_speed()))
print('Set gear to 3')
bike2.set_gear(3)
print('Current gear: ' + str(bike2.get_gear()))
print('Current speed: ' + str(bike2.get_speed()))
print('Set cadence to 45')
bike2.set_cadence(45)
print('Current cadence: ' + str(bike2.get_cadence()))
print('Current speed: ' + str(bike2.get_speed()))
print('Apply break 12')
bike2.apply_brakes(12)
print('Current speed: ' + str(bike2.get_speed()))
