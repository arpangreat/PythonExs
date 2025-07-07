
from PIL import Image
import numpy as np

def contrast_stretch(image_path, output_path):
    """
    Performs contrast stretching on an image.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the stretched image file.
    """
    try:
        # Open the image and convert to grayscale for a clear demonstration
        img = Image.open(image_path).convert('L')
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return

    # Convert image to a NumPy array for mathematical operations
    img_array = np.array(img, dtype=np.float64)

    # Get the min and max pixel values from the image
    min_in = np.min(img_array)
    max_in = np.max(img_array)

    # The desired output range
    min_out = 0.0
    max_out = 255.0

    # Apply the contrast stretching formula
    # (vectorized operation on the entire array)
    stretched_array = (img_array - min_in) * (
        (max_out - min_out) / (max_in - min_in)
    ) + min_out

    # Clip values to ensure they are within the 0-255 range
    # and convert back to an 8-bit integer format
    stretched_array = np.clip(stretched_array, 0, 255)
    stretched_array = np.uint8(stretched_array)

    # Create a new image from the stretched array
    stretched_img = Image.fromarray(stretched_array, 'L')

    # Save the new image
    stretched_img.save(output_path)
    print(f"Contrast stretched image saved to '{output_path}'")

# --- How to use it ---
if __name__ == '__main__':
    # Create a dummy low-contrast image for demonstration
    # This image will have pixel values from 50 to 150
    low_contrast_data = np.arange(50, 151, 1, dtype=np.uint8).reshape(1, -1)
    low_contrast_data = np.tile(low_contrast_data, (101, 1))
    low_contrast_img = Image.fromarray(low_contrast_data, 'L')
    low_contrast_img.save("low_contrast_example.png")

    print("Created a sample image: 'low_contrast_example.png'")

    # Now, apply the function to the image we just created
    contrast_stretch("low_contrast_example.png", "stretched_example.png")
