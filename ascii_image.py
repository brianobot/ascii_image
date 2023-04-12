import sys
import PIL.Image
from datetime import datetime


ASCII_CHARS = ["@", "#", '$', "%", "&", "?", "+",";", ":", ",", "."]


def resize_image(image, new_width=100):
    """function to resize an image object."""
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    """function to convert an image obj into grayscale coloration."""
    grayscale_image = image.convert("L")
    return grayscale_image


def pixel_to_ascii(image):
    """function to convert pixel to ascii characters"""
    pixels = image.getdata()
    characters = "".join(ASCII_CHARS[pixel//25] for pixel in pixels)
    return characters


def main(new_width=100):
    """Main function starts program execution."""
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        path = input("Enter a valid path to image: ")
        files = path.split(" ")
    images = []
    try:
        for file in files:
            image = PIL.Image.open(file)
            images.append(image)
    except: 
        print(file, ' is not a valid pathname to an image')  
    else:
        for index, image in enumerate(images):
            new_image_data = pixel_to_ascii(grayify(resize_image(image)))

            pixel_count = len(new_image_data)
            ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

            print(ascii_image)

            with open(f'{str(datetime.today().date())}_{index + 1}.txt', "w") as file:
                file.write(ascii_image)

    
if __name__ == "__main__":
    main()
