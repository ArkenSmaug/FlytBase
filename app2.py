import time
from flyt_python import api
from math import sqrt

drone = api.navigation(timeout = 120000)
side = 10
x_off = sqrt(side**2 - (side/2)**2)

time.sleep(3)

# Takeoff mode
print("Takeoff mode")
drone.take_off(10.0)

# Waypoint follow mode
print("Going along waypoints")
drone.position_set( 0     ,  side   , 0, relative = True)
drone.position_set( x_off , -side/2 , 0, relative = True)
drone.position_set(-x_off , -side/2 , 0, relative = True)

# Landing mode
print("Landing")
drone.land(async=False)

drone.disconnect()