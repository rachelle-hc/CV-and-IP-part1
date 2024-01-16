import cv2 as c
import pyautogui as p
import numpy as np

#create/capture resolution using p lib
rs=p.size()

#filename in which we store recording
fn=input("please enter any file name and path")
#fix the frame rate
fps=60.0

fourcc= c.VideoWriter_fourcc(*'XVID') #4byte codec which helps makes videos
#xvid format is better, and most reliable
output= c.VideoWriter(fn,fourcc,fps,rs)


c.namedWindow("Live_Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording",(600,400))

while True:
    img=p.screenshot()
    f = np.array(img)  #img is 2d array
    f = c.cvtColor(f,c.COLOR_BAYER_BGR2RGB)
    #normal computer sees rgb order:normal display
    #opencv/python reads in bgr
    
    output.write(f)
    c.imshow("Live_Recording",f)
    
    if c.waitKey(1) == ord("q"):
        break
    
    
    








