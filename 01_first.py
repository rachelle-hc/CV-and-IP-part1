import cv2 #opencv use as cv2 in python

print("matrix of 3channel")
img1=cv2.imread("C:\\Users\\dell\\Downloads\\forest.jpg",1) #use 1,0,-1 works only for imread fn, so ig not videos
#path if giving error, use double slashes or r'path_with_single_slashes or somethign else, forgot , ask chatg, or look ath video again
img1=cv2.resize(img1,(640,350)) #width, height
print(img1)
cv2.imshow("original",img1) #original is the window_name user puts


print("matrix of greyscale")
img2=cv2.imread("C:\\Users\\dell\\Downloads\\forest.jpg",0)
img2=cv2.resize(img2,(640,350)) #width, height
print(img2)
cv2.imshow("greyscale",img2)


print("matrix of unchanged/color saturation increased")
img3=cv2.imread("C:\\Users\\dell\\Downloads\\forest.jpg",-1)
img3=cv2.resize(img3,(640,350)) #width, height
print(img3)
cv2.imshow("unchanged",img3)
#increases color saturation of original image
#alpha channels changed

cv2.waitKey()
cv2.destroyAllWindows()
