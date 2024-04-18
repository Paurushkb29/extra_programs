#Write a python program to convert gray scale to rgb and rgb to gray scale.

from PIL import Image

def grayscale_to_rgb(grayscale_image_path, output_path):
    # Open the grayscale image
    grayscale_image = Image.open(grayscale_image_path)
    
    # Convert grayscale image to RGB
    rgb_image = grayscale_image.convert("RGB")
    
    # Save the RGB image
    rgb_image.save(output_path)
    
    print("Grayscale to RGB conversion successful.")

def rgb_to_grayscale(rgb_image_path, output_path):
    # Open the RGB image
    rgb_image = Image.open(rgb_image_path)
    
    # Convert RGB image to grayscale
    grayscale_image = rgb_image.convert("L")
    
    # Save the grayscale image
    grayscale_image.save(output_path)
    
    print("RGB to Grayscale conversion successful.")

# Example usage
# Paths to input and output images
input_grayscale_image_path = "grayscale_image.jpg"
output_rgb_path = "output_rgb_image.jpg"
output_grayscale_path = "output_grayscale_image.jpg"

# Convert grayscale image to RGB
grayscale_to_rgb(input_grayscale_image_path, output_rgb_path)

# Convert RGB image to grayscale
rgb_to_grayscale(output_rgb_path, output_grayscale_path)
