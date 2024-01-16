#to save it into memory

#read video from the webcame and then save into memeory


import cv2
videoname=cv2.VideoCapture(0) #0 for webcame, laptop primary cam,
#external webcam, external is 1

'''
if getting warning error, due to update after 3.8py,
if you are using below 3.8 version, you won't get warning
in that case, add parameter
videoname=cv2.VideoCapture(0,cv2.CAP_DSHOW)
'''


#DIVX,XVID,MJPG,X264,WMV1,WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID") # *"XVID" format or use any of the others
#It contains 4 parameters-name,codec,fps,resolution
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
#this will be saved wheerever your code is saved
#or you can put c drive, like ("C:\\output.avi",fourcc............
'''
if saving grayscale image, mention 0
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)


no need to metnion if color ==1,
but for gray , must metnion 0
'''



'''
videowriter saves it
output.avi" nmae and save it under that name, 
'''

while videoname.isOpened(): #this fn will alwasy return true as long as the webcam reads it
    #so ret value will also be true
        ret,frame=videoname.read()
        if ret==True:
            '''
            this is not needed as it is mentioned alr with video writer
            frame=cv2.resize(frame,(700,450))
            '''
            
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            frame=cv2.flip(frame,0) #computer webcam does weird reflective way
            cv2.imshow("original",frame)
            cv2.imshow("grayscale",gray)
            output.write(frame) #for color
           #output.write(gray) for grayscale save
            
            '''
            k=cv2.waitKey(25)
            if k == ord("q"):  # if k==.....q") &0xFF  <--mask if there is some error
                break
            
            below is alternate way
            '''
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #waitkey(0) means image, but (1) measn something dynamic, ie multiple frames,



videoname.release()
output.release() #if you don't free it, the video might get corrupted
cv2.destroyAllWindows()





