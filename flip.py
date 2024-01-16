import cv2 #opencv use as cv2 in python

img1=cv2.imread("C:\\Users\\dell\\Downloads\\forest.jpg",1)
img1=cv2.resize(img1,(640,350)) #width, height

img2=cv2.flip(img1,0) #reflection over x-axis
img3=cv2.flip(img1,1) #reflection over y-axis
img4=cv2.flip(img1,-1) #reflection over x-axis and then reflect over y-axis


cv2.imshow("original",img1)
cv2.imshow("r over x",img2)
cv2.imshow("r over y",img3)
cv2.imshow("r over x and then y",img4)


cv2.waitKey()
cv2.destroyAllWindows()