path=r'C:\Users\dell\Downloads\beachvideo.mp4'

import cv2
videoname=cv2.VideoCapture(path)
# print("beach",videoname)


while True:
    ret,frame=videoname.read()
    frame=cv2.resize(frame,(700,450))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #cvtColor is convert
    cv2.imshow("original",frame) #0,1,-1 is only for imread, so use this cvtColor fn tod irectly convert any frame to gray etc
    cv2.imshow("grayscale",gray)
    k=cv2.waitKey(25) #the lower the no, the playback speed increases, indirectly proportional
    #25 is normal playback
    if k == ord("q"):  # if k==.....q") &0xFF  <--mask if there is some error
        break


videoname.release()  #release the video
cv2.destroyAllWindows()
