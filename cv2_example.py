#Write a python program to read image, resize image, set the border color of the image using with cv2.

import cv2

def resize_with_border(image_path, output_path, target_size, border_color=(255, 255, 255), border_size=10):
    # Read the image
    image = cv2.imread(image_path)

    # Resize the image while maintaining aspect ratio
    resized_image = cv2.resize(image, target_size) #resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    
    # Add border to the resized image
    bordered_image = cv2.copyMakeBorder(resized_image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)
    
    # Save the image with borders
    cv2.imwrite(output_path, bordered_image)
    
    print("Image resized and bordered successfully.")

# Example usage
input_image_path = "input_image.jpg"
output_image_path = "output_image_with_border.jpg"
target_size = (300, 400)  # Target size for resizing
border_color = (0, 255, 0)  # Green color for border
border_size = 10

# Resize the image with border
resize_with_border(input_image_path, output_image_path, target_size, border_color, border_size)


# #Write a python program to read image, resize image, set the border color of the image using with cv2. 

# import cv2

# def resize_with_border(image_path, output_path, target_size, border_color=(255, 255, 255), border_size=10):
#     try:
#         # Read the image
#         image = cv2.imread(image_path)

#         # Resize the image while maintaining aspect ratio
#         resized_image = cv2.resize(image, target_size) #resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
        
#         # Add border to the resized image
#         bordered_image = cv2.copyMakeBorder(resized_image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)
        
#         # Save the image with borders
#         cv2.imwrite(output_path, bordered_image)
        
#         print("Image resized and bordered successfully.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_image_path = "input_image.jpg"
# output_image_path = "output_image_with_border.jpg"
# target_size = (300, 400)  # Target size for resizing
# border_color = (0, 255, 0)  # Green color for border
# border_size = 10

# # Resize the image with border
# resize_with_border(input_image_path, output_image_path, target_size, border_color, border_size)
