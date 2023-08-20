from PIL import Image, ImageEnhance

def resize_image(image, factor):
    width, height = image.size
    new_width = int(width * factor)
    new_height = int(height * factor)
    return image.resize((new_width, new_height))

def rotate_image(image, angle):
    return image.rotate(angle)

def mirror_image(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def display_image(image):
    image.show()

image_path = r'C:\Users\myahy\Desktop\R.bmp'
image = Image.open(image_path)

while True:
    print("Image Manipulation Options:")
    print("1. Rotate")
    print("2. Resize")
    print("3. Mirror")
    print("4. Adjust Brightness")
    print("5. Adjust Contrast")
    print("6. Display Image")
    print("7. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == "1":
        angle = float(input("Enter rotation angle (in degrees): "))
        image = rotate_image(image, angle)
    elif choice == "2":
        factor = float(input("Enter resizing factor (e.g., 0.5 for 50%): "))
        image = resize_image(image, factor)
    elif choice == "3":
        mirror_option = input("Mirror horizontally? (yes/no): ").lower()
        if mirror_option == "yes":
            image = mirror_image(image)
    elif choice == "4":
        factor = float(input("Enter brightness factor (0.1 to 2.0): "))
        image = adjust_brightness(image, factor)
    elif choice == "5":
        factor = float(input("Enter contrast factor (0.1 to 2.0): "))
        image = adjust_contrast(image, factor)
    elif choice == "6":
        display_image(image)
    elif choice == "7":
        print("Exiting the image editor.")
        break
    else:
        print("Invalid choice.")
