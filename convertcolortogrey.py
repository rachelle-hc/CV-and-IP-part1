#convert color to greyscale from user input

#  C:\\Users\\dell\\Downloads\\forest.jpg
#  C:\Users\dell\Downloads\lakeBW.jpg

path=input("Enter path:")
colorchoice=input("enter which choice: original or colored or greyscale or saturated image:")

print("the entered path is : ")
print("the image will be shown in: ", colorchoice)

#read image, resize image, edit image to -1,0,1, show image
#you can resize only after reading the images

import cv2

if colorchoice == "original" :    #original but little saturated
    img1=cv2.imread(path,-1)
    img1=cv2.resize(img1,(580,700))
    cv2.imshow("original",img1)
elif colorchoice == "colored" :
    img1=cv2.imread(path,1)
    img1=cv2.resize(img1,(580,700))
    cv2.imshow("colored",img1)
else:
    img1=cv2.imread(path,0)
    img1=cv2.resize(img1,(580,700))
    cv2.imshow("greyscale",img1)

print(img1)

k=cv2.waitKey()
if k==ord("s"):
    cv2.imwrite("C:\\Users\\dell\\Downloads\\outputinJPG.jpg",img1)
    cv2.imwrite("C:\\Users\\dell\\Downloads\\outputinPNG.png",img1)
else:
    cv2.destroyAllWindows()


'''
or
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''



