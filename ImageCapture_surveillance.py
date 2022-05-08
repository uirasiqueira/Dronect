from djitellopy import tello
import KeyModule as kp
from time import sleep
import cv2
import time

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = speed
    elif kp.getKey("d"):
        yv = -speed

    if kp.getKey("q"):
        me.land()
        time.sleep(3)
    if kp.getKey("e"):
        me.takeoff()

    if kp.getKey('z'): #when you click on z button it will take a picture
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img) #Create a new directory and inside directory a Image file
        time.sleep(0.3) #This function is to avoid generate too many pic whenever you click on z button

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))#resize window of video. Lower size
    cv2.imshow("Image", img) #Creating a window to display result
    cv2.waitKey(1) #If we dont add this function it frame will shut down before we see it