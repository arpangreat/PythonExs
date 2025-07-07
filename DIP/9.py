import cv2 
# Read and display an Image 
a=cv2.imread('image.jpg',0) 
# Bluring an Image(average) 
b = cv2.blur(a, (7,7)) 
# Bluring an Image(Gaussion) 
c=cv2.GaussianBlur(a,(7,7),0) 
cv2.imshow('Original Image',a) 
cv2.imshow('Bluring(average) Image',b) 
cv2.imshow('Bluring (Gaussian) Image',c) 
cv2.waitKey(0)  
cv2.destroyAllWindows()

