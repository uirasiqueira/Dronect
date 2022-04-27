from djitellopy import tello
import cv2


tel = tello.Tello()
tel.connect()
print(tel.get_battery())

tel.streamon()

while True:
    img = tel.get_frame_read().frame
    img = cv2.resize(img, (360,240))#resize window of video. Lower size
    cv2.imshow("Image", img) #Creating a window to display result
    cv2.waitKey(1) #If we dont add this function it frame will shut down before we see it

