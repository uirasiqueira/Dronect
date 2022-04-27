from djitellopy import tello
from time import sleep

tel = tello.Tello()
tel.connect() #Connect drone to PC
print(tel.get_battery()) #show % of battery


tel.takeoff()
tel.send_rc_control(0,5,0,0) #right/-left, forward/backwards,up/down, yaw (Angular velocity: rotation) [-100 to 100]
sleep(1)
tel.send_rc_control(0,0,0,700)
sleep(1)
tel.send_rc_control(0,0,0,0) #Same line code to make sure that drone will not be moving while landing
tel.land()