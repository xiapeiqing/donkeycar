# """ 
# My CAR CONFIG 

# This file is read by your car application's manage.py script to change the car
# performance

# If desired, all config overrides can be specified here. 
# The update operation will not touch this file.
# """
DRIVE_TRAIN_TYPE = "DRIVE_BY_WIRE_OVER_THE_AIR"
BLE_MAC_ADDR = "80:6F:B0:A7:F7:BF"
USE_JOYSTICK_AS_DEFAULT = True
CONTROLLER_TYPE='ps4'
JOYSTICK_MAX_THROTTLE = 1.0         #this scalar is multiplied with the -1 to 1 throttle value to limit the maximum throttle. This can help if you drop the controller or just
