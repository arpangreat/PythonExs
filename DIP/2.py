import cv2 
# Read an Image  
orginal_im=cv2.imread('image.jpg',1) 
cv2.imshow('Original Image',orginal_im) 
# Convert it into gray-scale image 
gray_im = cv2.cvtColor(orginal_im,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray Scale Image',gray_im) 
w,h=gray_im.shape 
print(w,h) 
# Resize(Reduced) an image 
reduced_size=(w//2,h//2) 
print(reduced_size) 
reduced_im = cv2.resize(gray_im,reduced_size,interpolation=cv2.INTER_CUBIC) 
cv2.imshow('Reduced Gray Image',reduced_im) 
# Resize(Enlarged) an image 
enlarged_size=(w*2,h*2) 
print(enlarged_size) 
enlarged_im = cv2.resize(gray_im, enlarged_size, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Enlarged Image',enlarged_im) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 


