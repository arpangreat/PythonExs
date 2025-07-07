import cv2 
# Load images using OpenCV 
image1 = cv2.imread('image.jpg',0)
print(image1.shape) 
print(image1.dtype) 
image2 = cv2.imread('image.jpeg',0)
print(image2.shape) 
w,h=image1.shape 
image2=cv2.resize(image2,(h,w), interpolation=cv2.INTER_CUBIC) 
print(image2.shape) 
cv2.imshow('1ST Image',image1) 
cv2.imshow('2nd Im age',image2) 
# Subtraction of an Image 
sub_im= image1 - image2 
cv2.imshow('Subtraction',sub_im) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

