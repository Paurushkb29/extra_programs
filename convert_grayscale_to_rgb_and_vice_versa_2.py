#Write a python program to convert gray scale to rgb and rgb to gray scale.

from PIL import Image
import matplotlib.pyplot as plt

def grayscale_to_rgb(grayscale_image_path, output_path):
    grayscale_image = Image.open(grayscale_image_path)
    rgb_image = grayscale_image.convert("RGB")
    rgb_image.save(output_path)
    print("Grayscale to RGB conversion successful.")
    return rgb_image

# Example usage
input_grayscale_image_path = "grayscale_image.jpg"
output_rgb_path = "output_rgb_image.jpg"

# Convert grayscale image to RGB
rgb_image = grayscale_to_rgb(input_grayscale_image_path, output_rgb_path)

# Display the RGB image
plt.imshow(rgb_image)
plt.axis('off')
plt.show()
