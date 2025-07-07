import cv2 
# Load images using OpenCV 
image1 = cv2.imread('image.jpg',0) 
image2 = cv2.imread('image.jpeg',0) # image1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)

# image2=cv2.cvtColor(image2,cv2.COLOR_BGR2RGB) 
w,h=image1.shape[:2] 
image2=cv2.resize(image2,(h,w), interpolation=cv2.INTER_CUBIC) 
print(image2.shape) 
print(image2.dtype) 
cv2.imshow('left_dog',image1) 
cv2.imshow('right_dog',image2) 
# add_im=cv2.add(image1,image2) 
# add_im = image1 + image2 
add_im= cv2.addWeighted(image1,0.5,image2,0.5,0) 
cv2.imshow('addition',add_im) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

