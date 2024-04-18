#Write a python program to convert the image to bw color and gray color using image module.

from PIL import Image

def convert_to_bw(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to black and white
    bw_image = image.convert("1")  # "1" mode indicates black and white
    
    # Save the black and white image
    bw_image.save(output_path)
    
    print("Image converted to black and white successfully.")

def convert_to_grayscale(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert("L")  # "L" mode indicates grayscale
    
    # Save the grayscale image
    grayscale_image.save(output_path)
    
    print("Image converted to grayscale successfully.")

# Paths to input and output images
input_image_path = "input_image.jpg"
output_bw_path = "output_bw_image.jpg"
output_grayscale_path = "output_grayscale_image.jpg"

# Convert image to black and white
convert_to_bw(input_image_path, output_bw_path)

# Convert image to grayscale
convert_to_grayscale(input_image_path, output_grayscale_path)
