from flyt_python import api
import time

drone = api.navigation(timeout=120000)
side = 6.5   #setting the side of the square

time.sleep(3)

# Take off mode of the drone
print("Taking Off")
drone.take_off(5.0)

# Waypoint following mode
print("Going along waypoints")
drone.position_set( side, 0.0, 0, relative = True)
drone.position_set( 0.0, side, 0, relative = True)
drone.position_set(-side, 0.0, 0, relative = True)
drone.position_set(0.0, -side, 0, relative = True)

# Landing mode
drone.land(async=False)

drone.disconnect()