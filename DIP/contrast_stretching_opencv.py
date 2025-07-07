
import cv2
import numpy as np

def contrast_stretch_opencv(image_path, output_path):
    """
    Performs contrast stretching on an image using OpenCV.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the stretched image file.
    """
    # Read the image in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: The file '{image_path}' could not be opened by OpenCV.")
        return

    # The cv2.normalize function can perform the stretching automatically.
    # It finds the min and max values and scales them to the specified range.
    # NORM_MINMAX specifies the normalization type.
    # The target range is 0-255 for an 8-bit image.
    stretched_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

    # Save the new image
    cv2.imwrite(output_path, stretched_img)
    print(f"Contrast stretched image saved to '{output_path}'")

    # Show the images
    cv2.imshow('Original Image', img)
    cv2.imshow('Stretched Image', stretched_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# --- How to use it ---
if __name__ == '__main__':
    # Create a dummy low-contrast image for demonstration
    # This image will have pixel values from 50 to 150
    low_contrast_data = np.arange(50, 151, 1, dtype=np.uint8).reshape(1, -1)
    low_contrast_data = np.tile(low_contrast_data, (101, 1))
    
    # Save the dummy image using OpenCV
    cv2.imwrite("low_contrast_example_cv2.png", low_contrast_data)
    print("Created a sample image: 'low_contrast_example_cv2.png'")

    # Now, apply the function to the image we just created
    contrast_stretch_opencv("low_contrast_example_cv2.png", "stretched_example_cv2.png")
